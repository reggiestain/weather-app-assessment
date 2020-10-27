## Django weather app

Django website that presents the current weather of the user's location
and also manages a list of notes.

## 1. Grab a copy of the project.

```bash

$ git clone https://github.com/reggiestain/WeatherApp.git

```

## 2. Create a virtual environment and install dependencies.

```bash

mkvirtualenv new_project
pip install -r requirements.txt

```

## 3. Create superuser.

You 'll need to create a new superuser for the admin to access the custom model.

```bash

python ./manage.py createsuperuser

```

## 4. Run the development server to verify everything is working.

```bash

python ./manage.py runserver

```
