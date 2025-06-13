from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category 
from .serializers import CategorySerializer

class ComputerAccessoriesView(APIView):
    def get(self,request):
        parent = Category.objects.get(slug='computer-accessories')
        subcategories = parent.subcategories.all()
        serializer = CategorySerializer(subcategories,many=True)
        return Response(serializer.data)
    
class LaptopAccessoriesView(APIView):
    def get 
