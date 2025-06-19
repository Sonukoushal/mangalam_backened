from rest_framework import serializers
from .models import Menu, Category , Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','menu']

class MenuSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True,read_only=True)

    class Meta:
        model = Menu
        fields = ['id','name','categories'] 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
