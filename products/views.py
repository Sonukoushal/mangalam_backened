from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Menu,Category,Product
from .serializers import MenuSerializer,CategorySerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSuperUserReadOnly


class MenuListCreateView(APIView):              
     permission_classes=[IsAuthenticated,IsSuperUserReadOnly] 

     def get(self,request):
          menus=Menu.objects.all()
          serializer = MenuSerializer(menus,many=True)
          return Response(serializer.data)  
     
     def post(self,request):
          serializer = MenuSerializer(data=request.data)
          if serializer.is_valid():  
               serializer.save() 
               return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

class MenuDetailView(APIView):
     permission_classes=[IsAuthenticated,IsSuperUserReadOnly]

     def get_object(self,pk):   
          try:           
               return Menu.objects.get(pk=pk)
          except Menu.DoesNotExist: 
               return None
          
     def get(self,request,pk):
          menu = self.get_object(pk)
          if not menu:  
               return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
          serializer = MenuSerializer(menu)
          return Response(serializer.data)
     

     def put(self,request,pk):
          menu = self.get_object(pk)
          if not menu:
               return Response({"error":"Not Found"},status=status.HTTP_404_NOT_FOUND)
          serializer = MenuSerializer(menu,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self,request,pk):
          menu=self.get_object(pk)
          if not menu:
               return Response({"error":"not found"},status=status.HTTP_404_NOT_FOUND)
          menu.delete()
          return Response({"message":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)
     
     
#Categories
class CategoryListCreateView(APIView):
     permission_classes=[IsAuthenticated,IsSuperUserReadOnly]

     def get(self,request):
          menu_id = request.GET.get('menu') 
                                            

          if menu_id:                                                            
              categories =  Category.objects.filter(menu__id=menu_id)              
          else:                                                                     
               categories = Category.objects.all()                                    
                                               
          serializer = CategorySerializer(categories,many=True) 
          return Response(serializer.data)
     
     def post(self,request):
          serializer= CategorySerializer(data=request.data)  
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)  
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
class CategoryDetailView(APIView):
     permission_classes = [IsAuthenticated, IsSuperUserReadOnly]

     def get_object(self,pk):
          try:
               return Category.objects.get(pk=pk)
          except Category.DoesNotExist:
               return None
          
     def get(self,request,pk):
          category = self.get_object(pk)
          if not category:
               return Response({"error":"not found"}, status=status.HTTP_404_NOT_FOUND)
          serializer = CategorySerializer(category)
          return Response(serializer.data)
     
     def put(self,request,pk):
          category = self.get_object(pk)
          if not category:
               return Response({"error":"not found"},status=status.HTTP_404_NOT_FOUND)
          serializer = CategorySerializer(category,data=request.data)

          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self,request,pk):
          category = self.get_object(pk)
          if not category:
               return Response({"error":"not found"},status=status.HTTP_404_NOT_FOUND)
          category.delete()
          return Response({"message":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)
     
class Productlistcreate(APIView):
     permission_classes=[IsAuthenticated,IsSuperUserReadOnly]

     def get(self,request):
          products= Product.objects.all()
          serializer = ProductSerializer(products , many=True)
          return Response(serializer.data)
     
     def post(self,request):
          serializer = ProductSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class ProductDetailView(APIView):
     permission_classes=[IsAuthenticated,IsSuperUserReadOnly]

     def get_object(self,pk):
          try:
               return Product.objects.get(pk=pk)
          except Product.DoesNotExist:
               return None
          
     def get(self,request,pk):
          product = self.get_object(pk)
          if not product:
               return Response({"error":"Not found"},status = status.HTTP_404_NOT_FOUND)
          serializer = ProductSerializer(product)
          return Response(serializer.data)
     
     def put(self,request,pk):
          product = self.get_object(pk)
          if not product:
               return Response({"error":"not found"}, status=status.HTTP_404_NOT_FOUND)
          serializer = ProductSerializer(product,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return  Response(serializer.data)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self,request,pk):
          product = self.get_object(pk)
          if not product:
               return Response({"error":"not found"},status=status.HTTP_404_NOT_FOUND)
          product.delete()
          return Response({"message":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)

     
                         
                         
          


                                                                          

     
