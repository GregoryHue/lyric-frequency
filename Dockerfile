
FROM node:20.16-bookworm

WORKDIR /usr/src/app

COPY . .

WORKDIR /usr/src/app/main/main/web/static_src

RUN npm install
RUN npm run build

FROM python:3.10-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY --from=0 /usr/src/app .

WORKDIR /usr/src/app/main

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations django
RUN python manage.py migrate

CMD ["gunicorn", "main.wsgi", "-b", "0.0.0.0:8000", "--workers", "1", "--access-logfile", "./gunicorn-logs.txt"]