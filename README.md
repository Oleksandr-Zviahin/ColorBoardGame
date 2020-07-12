# ColorBoardGame

## Prerequisites
- Python 3.7
- Django 3.0.8

## To start project as container you need docker and docker-compose
```bash
docker-compose up -d
```
and after it build you will able to see http://127.0.0.1:8000 index page   

## To start project as service you need to do next steps:

- Setup your virtual environment

- Install requirements
```bash
pip install -r requirements.txt
```

- Migrate database
```bash
python manage.py migrate
```

## Run Server

To start the server use:
```bash
python manage.py runserver
```