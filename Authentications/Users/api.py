from Users.models import Users
from rest_framework import viewsets, permissions

from .Serializers import UserSerializers

#Users viewSets
class UserssViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]

    serializer_class = UserSerializers

