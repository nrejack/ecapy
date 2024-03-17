#!/usr/bin/env python3

# cellular automata & Wolfram code


def generate_rules():
    # generate a dictionary of dictionaries indexed by Wolfram code
    # within each code, 8 possibilities (base 10) for transformation
    # based on group of 3 blocks
    rules = {}
    for i in range(256):
        mapping = {}
        num = str(bin(i))[2:].rjust(8, "0")
        for j in range(8):
            mapping[j] = num[7 - j]
        rules[i] = mapping
    return rules


def get_initial_state(width):
    # return block with only middle block in 1 state
    side_size = width // 2
    print(f"Side size set to: {side_size}")
    initial_state = "0" * side_size + "1" + "0" * side_size
    print(f"Initial state width: {str(len(initial_state))}")
    return initial_state


def iterate_state(curr, rule):
    # apply current rule to current state and return new state
    new_state = ""
    width = len(curr)
    new_state += curr[0]
    for i in range(0, width - 2):
        three_cells = "0b" + curr[i : i + 3]
        value = int(three_cells, 2)
        new_state += rule[value]
    new_state += curr[width - 1]
    return new_state


def textmode(binary_string):
    # format a 'binary string' into textmode for printing
    binary_string = binary_string.replace("1", "█")
    binary_string = binary_string.replace("0", " ")
    return binary_string


def webtextmode(binary_string, colorA, colorB):
    # format a 'binary string' into a web-printable text representation
    # TODO: improve this by coalescing large runs of same color
    # TODO: use blocks or something else
    binary_string = binary_string.replace("1", f"<span style='color:{colorA}'>█</span>")
    binary_string = binary_string.replace("0", f"<span style='color:{colorB}'>█</span>")
    return binary_string + "<br />"


def main():
    import shutil
    import logging

    logging.basicConfig(level=logging.INFO)
    term_size = shutil.get_terminal_size()
    term_col = term_size.columns
    logging.info(f"Terminal width (columns): {term_col}")
    width = term_col - 10
    if width % 2 == 0:
        width += 1
        logging.info("Added 1 to width to ensure seed is centered.")
    else:
        logging.info("Width is odd number of columns, not changing.")
    logging.info(f"Setting universe width to {width}")
    rules = generate_rules()
    rule_num = -1
    while rule_num == -1:
        rule_num = input("Select a rule (0-255): ")
        print(f"Entered: {str(rule_num)} Using value {str(rule_num := int(rule_num))}")
        if rule_num < 0 or rule_num > 255:
            print("Error: you must enter an integer between 0 and 255.")
            rule_num = -1
    trule = rules[rule_num]
    state = get_initial_state(width)
    # TODO: larger step numbers do not generate reliable output, fix
    steps = 100
    get_steps = 0
    get_steps = steps = input(
        "Enter the number of steps you would like to iterate (default: 100): "
    )
    if not get_steps:
        print(f"Invalid number of steps entered, using default {steps}")
    else:
        steps = int(get_steps)
        print(f"Entered {get_steps}, using value {steps}")
    print(f"Starting iteration ({steps} steps)\n")
    print(textmode(state))
    for i in range(steps - 1):
        state = iterate_state(state, trule)
        printable_state = textmode(state)
        print(printable_state)
    print("End")


if __name__ == "__main__":
    main()
