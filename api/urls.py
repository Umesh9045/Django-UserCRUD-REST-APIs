from django.urls import path
from api.views import get_users

urlpatterns = [
    path('users/', get_users, name='get_users'),
]