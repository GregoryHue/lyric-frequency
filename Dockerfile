FROM node:20.16-bookworm

WORKDIR /usr/src/app

COPY . .

WORKDIR /usr/src/app/main/main/web/static_src

RUN npm install
RUN npm run build

FROM python:3.12-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

EXPOSE 8000

WORKDIR /usr/src/app

COPY --from=0 /usr/src/app/main/requirements.txt .
RUN pip install -r requirements.txt

COPY --from=0 /usr/src/app .

WORKDIR /usr/src/app/main

RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations django
RUN python manage.py migrate
RUN python manage.py loaddata base_data.json

CMD ["gunicorn", "main.wsgi", "-b", "0.0.0.0:8000", "--workers", "1", "--threads", "2", "--timeout", "90", "--access-logfile", "./gunicorn-logs.txt"]