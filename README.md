

# Album Word Disparity


## Project setup

Install python libraries with:

```
cd main/
virtualenv --python="/usr/bin/python3" env 
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations django
python manage.py migrate
python manage.py tailwind install
```

## Usage

```
cd main/
source env/bin/activate
python manage.py runserver
python manage.py tailwind start
```

## Versions

- Python 3.10.12
- Scrapy 2.11.2

## Structure

```
main/
.gitignore
LICENSE
README.md
```

## References

- [Scrapy](https://scrapy.org/)
- [Genius](https://genius.com/)