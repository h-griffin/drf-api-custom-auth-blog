# Django rest framework with docker and postgreSQL token authorization & custom user


> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir drf-api-custom-auth-blog

Use poetry to initialize folder 

> $ cd `drf-api-custom-auth-blog` 
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


**post/views.py**
- import model, serializer, permissions
- list and detail view

**post/urls.py**
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

**post/tests.py**
- basic content test


#############################################

touch **project/.env** *INSIDE PROJECT FOLDER*

move settings to env
- rebuild after moving to env
> $ docker compose down 
> $ docker compose up --build -d

collect static files *INSIDE CONTAINER*
touch empty **static/** folder
    collect static needs static folder to create **staticfiles** folder

> $ python manage.py createsuperuser

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


############
  NOT DONE
############ 

httpie
> $ http POST :8000/api/token/ username=griffin password=12345

> $ http :8000/api/v1/ "Authorization: Bearer <'paste token'>"

postman website

superuser cannot see without token 
**library/settings**
```      'rest_framework.authentication.SessionAuthentication',
      'rest_framework.authentication.BasicAuthentication',
```
now the superuser can see without token
  browsable api (see without using django admin)



deploy through heroku or AWS -- tbd
next.js app will use live link ^^


deploy next through vercel


vercel errors: python and js allow, but connecting uses others that do not allow
    Link import 'next/Link' must be /link
        X import Link from 'next/Link'
        √ import Link form 'next/link'
                                 ^



