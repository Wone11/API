from Controllers.models import Controllers
from rest_framework import viewsets, permissions

from .Serializers import ControllerSerializers

#controllers viewSets
class ControllersViewSet(viewsets.ModelViewSet):
    queryset = Controllers.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]

    serializer_class = ControllerSerializers

