from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.get("/")
def root_page():
    return "How to use: call the API with /rule_number/iterations/, where 0 <= rule_number <= 255 and 0 <= iterations <= 1000. Known limitations: width currently fixed at 180 chars wide."


@app.get("/<int:rule>/<int:itercount>/")
def get_initial_params(rule, itercount):
    rule = int(escape(rule))
    itercount = int(escape(itercount))
    colors = get_colors()
    if rule < 0 or rule > 255:
        return "error: rule must be in range 0 - 255."
    elif itercount < 0 or itercount > 1000:
        return "error: iterations must be in range 0 - 1000"
    else:
        # TODO width currently fixed at 180
        # js: window.innerWidth could get dynamic val
        return eca_driver(180, rule, itercount, colors)

import random
from ecapybara import generate_rules, get_initial_state, iterate_state, webtextmode

def get_colors():
    # TODO: make this class attributes
    choice = random.random()
    if choice >= 0 and choice <= .333:
        colorA = "blue"
        colorB = "orange"
    elif choice > .333 and choice <= .666:
        colorA = "red"
        colorB = "green"
    elif choice > .666 and choice <= 1.0:
        colorA = "yellow"
        colorB = "purple"
    return (colorA, colorB)

def eca_driver(width: int, rule: int, itercount: int, colors: set):
    colorA = colors[0]
    colorB = colors[1]
    rules = generate_rules()
    state = get_initial_state(width)
    output = '<pre style="display:inline-block; line-height: 1em;">'
    trule = rules[rule]
    for i in range(itercount):
        output += webtextmode(state, colorA, colorB)
        state = iterate_state(state, trule)

    return output + "</pre>"


# TODO add links back and forth between rules
