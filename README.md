

# Album Word Disparity

Album Word Disparity is a web-application that lets you search for an album and displays the occurrence of each word in the album.

<p align="center">
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

### Dev

Set `DJANGO_ENV=dev` in the `.env` file. Then start the server with:

```bash
python manage.py runserver
```

To update CSS change, in a second terminal:

```bash
python manage.py tailwind start
```

Or just start a crawl with:

```bash
python manage.py crawl -S "[artist_name]" -A "[album_name]"
```

### Docker

To start your first container:

```bash
docker build -t awd . && docker run --name awd -itd -p 80:8000 awd -e "DJANGO_ENV=prod" -e "DJANGO_SECRET_KEY=[A DJANGO SECRET KEY]"
```

To restart it:

```bash
docker stop awd && docker remove awd && docker build -t awd . && docker run --name awd -itd -p 80:8000 awd -e "DJANGO_ENV=prod" -e "DJANGO_SECRET_KEY=[A DJANGO SECRET KEY]"
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
.gitignore
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