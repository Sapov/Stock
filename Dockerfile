FROM python:latest
LABEL authors="Sapov"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt update && apt -qy install vim cron
RUN useradd -rms /bin/bash django && chmod 777 /opt /run
WORKDIR /django
RUN mkdir /django/static
RUN mkdir /django/media
RUN chmod -R django:django /django && chmod 755 /django
COPY --chown=django:django . .
RUN pip install -r requariments.txt
USER django
CMD ["gunicorn","-b","0.0.0.0:8000","mysite.wsgi:application"]