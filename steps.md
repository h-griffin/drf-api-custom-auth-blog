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
> $ poetry shell 

> $ django-admin startproject blog_project .
> $ python manage.py startapp post

**do not migrate until user model is authenticated with admin**

**pyproject.toml**
```python = "~3.8"```

### POST ### 
- models
- admin
    model
- settings > installed apps
    post app
- project urls
    post app urls > create urls.py
        views
            models
            serializers
                model
            permissions
    jwt token views

- settings > installed apps
    whitenoise
    djnago
    rest
    cors
- settings > middleware
    cors 
    whitenoise
- settings > databases
- settings > add manually 
    statics
    rest framework
    cors whitelist
tests


### USERS ### 
touch users/

models
admin
    models
    forms
settings > installed apps
    users app

project > urls
    users app urls
        views
            models
            serializers
tests



#############################################

**post/models.py**
- class Post

**post/admin.py**
- register Post

touch **post/permissions.py**
- read only for view write only for author

touch **post/serializers.py**


**recipes/views.py**
- import model, serializer, permissions
- list and detail view

**recipes/urls.py**
- home  =  list
- int   =  detail

**project/settings.py**
- convert to future env
- installed apps
- middleware
- databases

**project/urls.py**
- import jwt
- app urls
- authorization - token - token refresh

**recipes.tests.py**
- basic content test

made superuser


touch **Dockerfile**
touch **docker-compose.yml**
touch **requirements.txt**
> $ poetry export -f requirements.txt -o requirements.txt

> $ docker-compose up -d

**Dockerfile**
```FROM python:3.8-slim``` slim!!

**project/settings.py**
- set static root

> $ python manage.py collectstatic 
    - empty static/ and will create staticfiles/

> $ poetry export -f requirements.txt -o requirements.txt

