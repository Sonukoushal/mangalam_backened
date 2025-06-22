from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Favourite
from .serializers import FavoriteSerializer
from products.models import Product

class FavouriteView(APIView):
    permission_classes={IsAuthenticated}

    def get(self,request):
        favourites = Favourite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favourites,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        product_id= request.data.get('product')
        try:
            product = Product.objects.get(id=product_id)
            fav, created= Favourite.objects.get_or_create(user=request.user,product=product)
            if created:
                return Response({"message":"Added to favourite"},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"Already in favourites"},status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error":"Product not found"},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request):
        product_id=request.data.get('product')
        try:
            fav=Favourite.objects.get(user=request.user,product__id=product_id)
            fav.delete()
            return Response ({"message":"removed from favourites"})
        except Favourite.DoesNotExist:
            return Response({"error":"favourite not found"},status=status.HTTP_404_NOT_FOUND)

    