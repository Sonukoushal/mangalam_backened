from rest_framework import serializers
from .models import Favourite
from products.serializers import ProductSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Favourite 
        fields = ['id','product','added_at']
        