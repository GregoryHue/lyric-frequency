

# Lyric Frequency

Lyric Frequency is a web-application that lets you search for an album and displays the occurrence of each word in the album.

[https://lyric-frequency.onrender.com/](https://lyric-frequency.onrender.com/)

*Note: If you come across an error 502, it is because of a lack of memory. The best way to test this project is locally with Docker.*

<p align="center" style="padding-top: 12px;">
  <img src="https://github.com/GregoryHue/lyric-frequency/blob/main/main/main/web/static_src/src/screenshot.jpg?raw=true" alt="Lyric Frequency Screenshot"/>
</p>

## Setup for dev

Create a `.env` file at the root of the project and complete it:

```bash
touch .env
nano .env
```

```bash
DJANGO_SECRET_KEY=[A DJANGO SECRET KEY]
DJANGO_ENV=dev
```

Setup the project:

```bash
virtualenv --python="/usr/bin/python3" env 
source env/bin/activate
cd main/
pip install -r requirements.txt
python manage.py tailwind install
python manage.py makemigrations django
python manage.py migrate
```

Then, in a first terminal, start tailwind to update any CSS change:

```bash
python manage.py tailwind start
```

In a second terminal, start the server:

```bash
python manage.py runserver
```

## Setup for Docker

Create a `.env` file at the root of the project and complete it:

```bash
touch .env
nano .env
```

```bash
DJANGO_SECRET_KEY=[A DJANGO SECRET KEY]
DJANGO_ENV=prod
```

Then, start your first container:

```bash
docker build -t lf . && docker run --name lf -itd -p 80:8000 lf
```

Go to [http://localhost](http://localhost).

## Versions

- Python 3.10.12
- Node 20.12.2
- Scrapy 2.11.2
- Plotly 5.23.0

## Structure

```
main/
  main/
    django/     -- backend 
    scraper/    -- crawl data from Genius
    web/        -- frontend 
.dockerignore
.gitignore
Dockerfile
LICENSE
README.md
```

## References

- [Genius](https://genius.com/)
- [Django](https://www.djangoproject.com/)
- [Django Secret Key Generator](https://djecrety.ir/)
- [Django Tailwind](https://django-tailwind.readthedocs.io/en/latest/index.html)
- [Tailwind CSS](https://tailwindcss.com/)
- [Scrapy](https://scrapy.org/)
- [scrapy-djangoitem](https://pypi.org/project/scrapy-djangoitem/)
- [Plotly Open Source Graphing Library for Python](https://plotly.com/python/)
- [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/)
- [Stack Overflow - Scrapy 'ReactorNotRestartable' error](https://stackoverflow.com/questions/45137458/scrapy-twisted-internet-error-reactornotrestartable-error-after-first-run)
- [Docker](https://www.docker.com/)
- [Render](https://render.com/)
- [Docker on Render](https://docs.render.com/docker)
- [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)