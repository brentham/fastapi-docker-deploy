fastapi-project
├── alembic/
├── config  # db connection
│   │   ├── database.py
│   │   ├── config.py
│   │   └── utils.py
├── src
│   ├── auth
│   │   ├── main.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   │   ├── dependencies.py
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   └── feature-1
│   │   ├── main.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   └── feature-2
│   │   ├── main.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
|   |    __init__.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   └── main.py
├── tests/
│   ├── auth
│   ├── azure
│   └── feature-1
│   └── feature-2
├── templates/
│   └── index.html or jinja
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
└── pyproject.toml
└── poetry.lock