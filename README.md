

# Album Word Disparity


## Project setup

Install python libraries with:

```
virtualenv --python="/usr/bin/python3" env 
source env/bin/activate
cd main/
pip install -r requirements.txt
```

## Usage

```
source env/bin/activate
cd main/
scrapy crawl album -O data.json
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