from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','name','password']
        extra_kwargs = {
            'password': {'write_only': True}  # password user ko visible na ho
        }
    def create(self, validated_data):   #validated_data ek dictionary hai jisme woh data hota hai jo client (Postman ya frontend) se aaya tha
                                         #Aur serializer.is_valid() hone ke baad validate ho chuka hota hai.
        user =CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )
        return user 