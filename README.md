

# Album Word Disparity


## Project setup

Set up the project with:

```
virtualenv --python="/usr/bin/python3" env 
source env/bin/activate
cd main/
pip install -r requirements.txt
python manage.py makemigrations django
python manage.py migrate
python manage.py tailwind install
```

## Usage

Start the server with:

```
source env/bin/activate
cd main/
python manage.py runserver
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