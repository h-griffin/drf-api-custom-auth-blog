# Django rest framework with docker and postgreSQL token authorization & custom user


> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir drf-auth-blog

Use poetry to initialize folder 

> $ cd `drf-auth-blog` 
> $ poetry init -n 
> $ poetry add django djangorestframework 
> $ poetry add --dev black 
> $ poetry shell 

> $ django-admin startproject blog_project .
> $ python manage.py startapp post

# ! CHECKLIST ! 
**pyproject.toml**
```[tool.poetry.dependencies]
python = "~3.8"
django = "^3.0.7"
djangorestframework = "^3.11.0"
whitenoise = "^5.1.0"
django-cors-headers = "^3.4.0"
djangorestframework-simplejwt = "^4.4.0"
psycopg2-binary = "^2.8.5"
django-environ = "^0.4.5"
gunicorn = "^20.0.4"
```

**do not migrate until user model is authenticated with admin**

**project/settings.py**
INSTALLED_APPS = ```'post.apps.PostConfig',```
AUTH_USER_MODEL = ```post.CustomUser```

models
admin









**Dockerfile**
```FROM python:3.8-slim``` slim!!

**project/settings.py**
- set static root

> $ python manage.py collectstatic 
    - empty static/ and will create staticfiles/

> $ poetry export -f requirements.txt -o requirements.txt

