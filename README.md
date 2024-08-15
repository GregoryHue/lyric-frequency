

# Album Word Disparity

<p align="center">
  <img src="https://github.com/GregoryHue/album-word-disparity/blob/main/main/main/web/static_src/src/screenshot.jpg?raw=true" alt="Album Word Disparity Screenshot"/>
</p>

## Project setup

Create a .env file at the root of the project and complete it:

```bash
touch .env
```

```bash
SECRET_KEY=[A DJANGO SECRET KEY]
ENV=[dev OR prod]
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

Start the server with:

```bash
source env/bin/activate
cd main/
python manage.py runserver
```

To update CSS change, in a second terminal:

```bash
source env/bin/activate
cd main/
python manage.py tailwind start
```

Or just start a crawl with:

```bash
cd main/
source env/bin/activate
python manage.py crawl -S "[artist_name]" -A "[album_name]"
```

## Versions

- Python 3.10.12
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
- [Django Tailwind](https://django-tailwind.readthedocs.io/en/latest/index.html)
- [Tailwind CSS](https://tailwindcss.com/)
- [Scrapy](https://scrapy.org/)
- [scrapy-djangoitem](https://pypi.org/project/scrapy-djangoitem/)
- [Plotly Open Source Graphing Library for Python](https://plotly.com/python/)
- [Stack Overflow - Scrapy 'ReactorNotRestartable' error](https://stackoverflow.com/questions/45137458/scrapy-twisted-internet-error-reactornotrestartable-error-after-first-run)
- [Deploy a Django App on Render](https://docs.render.com/deploy-django#updating-an-existing-django-project)
- [PostgreSQL](https://doc.ubuntu-fr.org/postgresql)