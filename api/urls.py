from django.urls import path
from api.views import create_user, delete_user, get_users, update_user

urlpatterns = [
    path('users/', get_users, name='get_users'),  # GET all users
    path('users/create/', create_user, name='create_user'),  # POST new user
    path('users/<int:user_id>/update/', update_user, name='update_user'),  # PUT update user
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),  # DELETE user
]