FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
# ENV PYTHONPATH=/app

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi --no-root

WORKDIR /src
