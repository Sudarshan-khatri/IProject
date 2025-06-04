from rest_framework import serializers
from ..models import CustomUser

class RegisterationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'



class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password']



