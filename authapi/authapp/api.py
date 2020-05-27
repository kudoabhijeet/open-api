from authapp.models import users
from rest_framework import viewsets, permissions
from .serializers import usersSerializer

# users viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = usersSerializer