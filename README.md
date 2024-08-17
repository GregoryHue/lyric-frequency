

# Album Word Disparity

Album Word Disparity is a web-application that lets you search for an album and displays the occurrence of each word in the album.

[Deployed demo](https://album-word-disparity.onrender.com/)

<p align="center" style="padding-top: 12px;">
  <img src="https://github.com/GregoryHue/album-word-disparity/blob/main/main/main/web/static_src/src/screenshot.jpg?raw=true" alt="Album Word Disparity Screenshot"/>
</p>

## Project setup

Create a .env file at the root of the project and complete it:

```bash
touch .env
```

```bash
DJANGO_SECRET_KEY=[A DJANGO SECRET KEY]
DJANGO_ENV=[dev OR prod]
```

Set up the project with:

```bash
virtualenv --python="/usr/bin/python3" env 
source env/bin/activate
cd main/
pip install -r requirements.txt
python manage.py tailwind install
python manage.py makemigrations django
python manage.py migrate
```

## Usage

### For local dev

Set `DJANGO_ENV=dev` in the `.env` file. Then, in a first terminal, start tailwind to update any CSS change:

```bash
python manage.py tailwind start
```

In a second terminal, start the server:

```bash
python manage.py runserver
```

### For a Docker container

Set `DJANGO_ENV=prod` in the `.env` file. Then, start your first container:

```bash
docker build -t awd . && docker run --name awd -itd -p 80:8000 awd
```

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