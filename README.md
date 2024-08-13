

# Album Word Disparity

<p align="center">
  <img src="https://github.com/GregoryHue/album-word-disparity/blob/main/main/main/web/static_src/src/screenshot.jpg?raw=true" alt="Album Word Disparity Screenshot"/>
</p>

## Project setup

Set up the project with:

```
virtualenv --python="/usr/bin/python3" env 
source env/bin/activate
cd main/
pip install -r requirements.txt
python manage.py tailwind install
```

Set up the database with:

```
sudo apt install postgresql
sudo -i -u postgres
```

Get into the SQL command prompt:

```
psql
```

Create our user:

```
CREATE ROLE awd_user LOGIN;
ALTER ROLE awd_user CREATEDB;
CREATE DATABASE awd_db OWNER awd_user;
ALTER ROLE awd_user WITH ENCRYPTED PASSWORD '[POSTGRES_PASSWORD]';
```

*Note: the POSTGRES_PASSWORD needs to be set in a .env file, at the root of the project*

```
python manage.py makemigrations django
python manage.py migrate
```

## Usage

Start the server with:

```
source env/bin/activate
cd main/
python manage.py runserver
```

To update CSS change, in a second terminal:

```
source env/bin/activate
cd main/
python manage.py tailwind start
```

Or just start a crawl with:

```
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