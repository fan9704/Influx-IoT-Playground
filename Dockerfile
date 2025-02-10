FROM python:3.12.5-slim

RUN pip install poetry
RUN poetry config virtualenvs.in-project true --local

WORKDIR /app
COPY poetry.lock pyproject.toml ./
COPY . /app

RUN poetry install
ENV MQTT_SERVER_IP="127.0.0.1"
ENV DEVICE_NUMBER=3

CMD ["poetry","run","python3", "main.py"]