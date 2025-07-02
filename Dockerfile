FROM python:3.10.5

WORKDIR /app/src/app

COPY pyproject.toml .

RUN pip install poetry 
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

COPY . .

ENV PYTHONPATH=/app/src


ENTRYPOINT ["python"]

