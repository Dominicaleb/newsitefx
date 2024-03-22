FROM python:3.11.4-slim-bullseye
WORKDIR /webapp

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /webapp

ENTRYPOINT [ "gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]
