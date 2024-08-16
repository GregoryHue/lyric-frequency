FROM python:3.10-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

WORKDIR /usr/src/main

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py tailwind install
RUN python manage.py tailwind build
RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations django
RUN python manage.py migrate

CMD ["gunicorn", "main.wsgi", "-b", "0.0.0.0:8000"]