from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()  # Get all users from the database
    serializer = UserSerializer(users, many=True)  # Convert to JSON
    # return Response(serializer.data)  # Send response
    return Response(UserSerializer({'name': "Umesh", 'age': 21}).data)
