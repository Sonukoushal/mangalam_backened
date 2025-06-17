from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Menu,Category,Product
from .serializers import MenuSerializer,CategorySerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSuperUserReadOnly

#Menu Button
class MenuListCreateView(APIView):              #API inbuilt class hai or permission_classes predefined variable 
     permission_classes=[IsAuthenticated,IsSuperUserReadOnly] #IsAuthenticated ➝ Ensure karta hai ki user login karke token pass kare

     def get(self,request):#self ka matlab hota hai — "ve object jisne method call kiya hai
          menus=Menu.objects.all()#menus ek variable hai jisme Menu jo ki models me ek table hai or  .objects.all() ek inbuilt query function hai jo aapke model ke table se sara data laata hai.
          serializer = MenuSerializer(menus,many=True)#serializer ek variable(vese object hai kyuki class ka instance ban raha hai )(menus-object jisme Menu model ka sara data hai,many=True kyuki multiple items hai)
          return Response(serializer.data)  #serializer vo object jisme .data(jo ki rest framework ki inbuilt property hai ) matlab sara data response me bheja jaa raha hai
     
     def post(self,request):
          serializer = MenuSerializer(data=request.data)#yaha data inbuilt parameter ha drf ka .data ka matlab sara data jo ki request se aya hai
          if serializer.is_valid():  #.is_valid ye DRF ka inbuilt hai 
               serializer.save() #.save bhi 
               return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     #Response DRF ka inbuilt function hai jo ki json  response deta hai

class MenuDetailView(APIView):
     permission_classes=[IsAuthenticated,IsSuperUserReadOnly]

     def get_object(self,pk):   
          try:           #jaha koi hume condition di gayi ho vaha if or else ka use lekin jah sambhavna hai ki error aa sakti hai vaha try or except ka use 
               return Menu.objects.get(pk=pk)#Menu naam ka model .object model ka manager hai jiske through hum database me query karte hai 
          except Menu.DoesNotExist: #.get ek inbuilt method hai jo specific value return kart hai object method ko left pk=model ka field name right pk = argumrnt to parameter of function
               return None
          
     def get(self,request,pk):
          menu = self.get_object(pk)#.get_object naam ka method call ho raha hai jisme pk id diya gaya hai or vo pk menu me save ho jayegi 
          if not menu:  #not logical operator jo ki condition ko ulta kar deta hai true ya false me 
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
          menu_id = request.GET.get('menu') #request.GET → ek dictionary hoti hai jo URL ke query parameters ko hold karti hai.
                                            #.get('menu') → us dictionary me se 'menu' key ka value nikalta hai.

          if menu_id:                                                             #http://127.0.0.1:8000/categories/?menu=2
              categories =  Category.objects.filter(menu__id=menu_id)              #?menu=2 → query parameter hai
          else:                                                                     # menu → key hai
               categories = Category.objects.all()                                    #2 → value hai
                                               
          serializer = CategorySerializer(categories,many=True) 
          return Response(serializer.data)
     
     def post(self,request):
          serializer= CategorySerializer(data=request.data)  #request.data postman/frontend se aya hua data
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)  #serializer.data = Clean, validated output data to frontened
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

     
                         
                         
          


                                                                          

     