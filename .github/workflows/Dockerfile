FROM python:3.12.3-slim


RUN pip install poetry==1.8.3

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry config virtualenvs.create false && poetry install --only main --no-root --no-interaction --no-ansi

COPY ./src ./src/

WORKDIR /app/src

# RUN poetry install --only main --no-root --no-interaction --no-ansi

EXPOSE 80

CMD [ "poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80", "main:app" ]


















# FROM python:3.12.3-slim AS builder

# RUN apt update && apt install curl -y

# # RUN pip install poetry==1.8.3
# RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
#     cd /usr/local/bin && \
#     ln -s /opt/poetry/bin/poetry && \
#     poetry config virtualenvs.create false

# WORKDIR /app

# COPY ./pyproject.toml ./poetry.lock* /app/

# RUN poetry config virtualenvs.create false && poetry install --only main --no-root --no-interaction --no-ansi

# COPY ./app ./app/

# FROM python:3.12.3-slim

# # RUN apt update && apt install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
# RUN rm -rf /var/lib/apt/lists/*

# COPY --from=builder /app /app

# WORKDIR /app

# # RUN apt update && apt install curl -y

# RUN pip install poetry==1.8.3
# # RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
# #     cd /usr/local/bin && \
# #     ln -s /opt/poetry/bin/poetry && \
# #     poetry config virtualenvs.create false

# RUN poetry install --only main --no-root --no-interaction --no-ansi

# EXPOSE 80

# CMD [ "poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80", "app.main:app" ]