# Django REST API Setup Guide

## Create and Activate Virtual Environment
```sh
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# To deactivate virtual environment
# Run:
deactivate
```

## Install Django and Django REST Framework
```sh
pip install django djangorestframework
```

## Create a Django Project
```sh
django-admin startproject newproject
cd newproject
```

## Create an App for APIs
```sh
python manage.py startapp api
```

## Configure `settings.py`
- Add the app and REST framework to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
```

## Create a Model (User)
- In `api/models.py`:
```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

- Run migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

## Create a Serializer (JSON Converter)
- In `api/serializers.py`:
```python
#in api folder
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
```


## Define API URLs
- In `api/urls.py`:
```python
urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
]
```

- Update `newproject/urls.py`:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

## Run the Server and Test APIs
```sh
python manage.py runserver
```

---
