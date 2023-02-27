from rest_framework import serializers
from Users.models import Users

'''Controller Serializers'''
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'
        