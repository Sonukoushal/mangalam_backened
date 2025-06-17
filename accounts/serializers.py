from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):  #Model ke data ko JSON me convert karna (read karne ke liye) or JSON data ko validate karna aur Python object me badalna (write karne ke liye)
    class Meta:                       # "Python object me badalna" ka matlab hota hai: #Frontend se aayi string/text wali information ko Python dict ya model object me convert karna — taaki hum uske saath Python code me kaam kar sakein.
        model = CustomUser
        fields = ['email','name','password']
        extra_kwargs = {
            'password': {'write_only': True}  
        } 
    def create(self, validated_data):     #jab bhi hum custom model  banate hai to to hume ek function lagana padta hai validated_data parameter ke sath
                                           #validated_data ek dictionary hai 
        user =CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )
        return user 