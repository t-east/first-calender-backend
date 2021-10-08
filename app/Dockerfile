FROM python:3.8.12-slim
WORKDIR /app
RUN apt-get -y update && \
  apt-get autoremove -y && \
  apt-get clean
ENV LANG en_US.utf8
COPY pyproject.toml poetry.lock /app/
RUN python3.8 -m pip install --no-cache-dir poetry && \
  poetry config virtualenvs.create false && \
  poetry install && \
  rm pyproject.toml poetry.lock