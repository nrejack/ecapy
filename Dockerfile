from python:3.10-slim

WORKDIR /usr/src/app
COPY app.py ./
COPY ecapybara.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

