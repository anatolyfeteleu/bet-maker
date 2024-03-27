FROM python:3.12

# [set working directory]
WORKDIR /app/code

# [set environment variables]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

ENV SCRIPTS_PATH=./_compose/scripts
ENV PROJECT_PATH=/app/code

# [updating packages]
RUN apt update -y

# [copying scripts]
COPY $SCRIPTS_PATH/start-app /
RUN chmod +x /start-app

# [installing requirements]
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-input setuptools poetry

COPY pyproject.toml poetry.lock /

RUN poetry config virtualenvs.create false
RUN poetry install

# [copying codebase]
ADD . $PROJECT_PATH