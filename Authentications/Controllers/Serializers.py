from rest_framework import serializers
from Controllers.models import Controllers

'''Controller Serializers'''
class ControllerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Controllers
        fields='__all__'
        