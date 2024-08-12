FROM python:latest
LABEL authors="Sapov"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt update && apt -qy install vim cron

