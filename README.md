# Django-UserCRUD-REST-APIs# Django Project Setup Guide

## 1. Create a Python Virtual Environment
```sh
python -m venv .venv
```

## 2. Activate the Virtual Environment
- **Windows**:
  ```sh
  .venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```sh
  source .venv/bin/activate
  ```

## 3. Install Django and Django REST Framework
```sh
pip install django djangorestframework
```

## 4. Create Django Project `newproject`
```sh
django-admin startproject newproject
```

## 5. Navigate to the Project Directory
```sh
cd newproject
```

## 6. Create Django Apps
```sh
python manage.py startapp api
```

## 7. Configure `settings.py`
- Add the created app and Django REST Framework to `INSTALLED_APPS`:
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
- Configure Database, Middleware, and Static files as needed.

## 8. Create Models and Perform Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

## 9. Create `serializers.py`
- Serializers convert data into JSON for APIs:
  ```python
  from rest_framework import serializers
  
  class UserSerializer(serializers.Serializer):
      name = serializers.CharField(max_length=100)
      age = serializers.IntegerField()
  ```

## 10. Create `views.py`
- Define API views using Django REST Framework:
  ```python
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from .serializers import UserSerializer
  
  @api_view(['GET'])
  def get_user(request):
      return Response(UserSerializer({'name': "Umesh", 'age': 21}).data)
  ```

## 11. Configure URL Handling
- Update `urls.py`:
  ```python
  from django.urls import path
  from api.views import get_user
  
  urlpatterns = [
      path('users/', get_user, name='get_user'),
  ]
  ```

## 12. Run the Development Server
```sh
python manage.py runserver
```

## 13. Create a Superuser (for Admin Panel)
```sh
python manage.py createsuperuser
```

## 14. Run Tests
```sh
python manage.py test
```

## 15. Deactivate the Virtual Environment (if needed)
```sh
deactivate
```
