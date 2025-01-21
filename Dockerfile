FROM python

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry config virtualenvs.create false && poetry install --only main --no-root --no-interaction --no-ansi

COPY ./src ./src/

WORKDIR /app/src

EXPOSE 8000

CMD [ "poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "main:app" ]
# CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "443", "--reload" ]