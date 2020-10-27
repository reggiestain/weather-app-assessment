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

## 3. Duplicate new_project/new_project/local_settings_example.py and save as local_settings.py.

## 4. Enter your database settings in local_settings.py.

## 5. Initialize your database.

```bash

python ./manage.py syncdb
python ./manage.py migrate

```

You 'll need to create a new superuser for the admin to access the custom note model.

```bash

python ./manage.py createsuperuser

```

## 6. Run the development server to verify everything is working.

```bash

python ./manage.py runserver

```
