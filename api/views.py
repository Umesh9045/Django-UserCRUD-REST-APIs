from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()  # Get all users from the database
    serializer = UserSerializer(users, many=True)  # Convert to JSON
    return Response(serializer.data)  # Send response
    # return Response(UserSerializer({'name': "Umesh", 'age': 21}).data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Find the user
    serializer = UserSerializer(user, data=request.data)  # Update with new data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Find the user
    user.delete()  # Remove from database
    return Response({"message": "User deleted successfully"}, status=204)