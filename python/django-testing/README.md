# About

Django minimal example application and testing experiments.


# Requirements

`VENV` - environmental variable containing the virtual environment path

`PROJECT_ROOT_DIR` - top project root directory

- Virtual environment

- pip

Once the virtual environment is installed, set it up in the `VENV` directory:
 
- `virtualenv venv`

activate it and verify:

- `source $ENV/bin/activate`
- `which pip` - points to the `VENV` directory
- `python -c "import django; print(django.get_version())"`

Install requirements:

`pip install -r requirements.txt`


# Project set up

- `source $ENV/bin/activate`

- `django-admin startproject MYPROJECT`

The automatically created files locations were manipulated with
and the paths in the files *adjusted*.

- description of the projects's created
  [here](files: https://docs.djangoproject.com/en/1.8/intro/tutorial01)

These files will already work as a first simple application
themselves - test that the files are functional and that the
application loads - start the development server.


Create a web application within the projects into which the 
business logic will be implemented:
 
```bash
cd $PROJECT_ROOT_DIR
python manage.py startapp pollsapp
```
 
This creates views, models, etc empty files.


## Database set up - PostgreSQL

- start and set up database (see `settings.py`) (database user):

```bash
createdb myapp_experiment
psql myapp_experiment
```

On the opened PostgreSQL console:

```
create user myapp_user with password 'VERY_c0nfid3nti1l';
alter database myapp_experiment owner to myapp_user;
alter user myapp_user CREATEDB;  # will be creating databases during testing
```

Set up schema for the requisite Django components (as defined in `settings.py`):

`python manage.py migrate`

# Start the development server

`python manage.py runserver 8080`

# Testing

For testing Django we use [py.test](http://pytest.org/).



# Assorted notes

## Force re-running a migration

We want to run a previously run existing migration `0002`. So we'll fake the
migrations to `0001`:

```bash
python manage.py migrate --fake pollsapp 0001
python manage.py migrate
```