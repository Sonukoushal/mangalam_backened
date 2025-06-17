from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status  
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework.authentication import TokenAuthentication


class PromoteSuperuser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,user_id):
        if not request.user.is_superuser:
            return Response({"error":"access deneid"},status=403)
        
        try:
            user = CustomUser.objects.get(id=user_id)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return Response({"message": f"{user.email} is now a superuser"})
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)


class SignupView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():   #ye chalte hi validated_data me user ne jo data input diya hai vo aa jata hai 
            user = serializer.save()  #yaha user(serializer vale) ne apne aap ko return kiya hai 

             # JWT Token Generate karo
            refresh = RefreshToken.for_user(user)
            token_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({
                'msg': 'Signup successful ',
                'user': serializer.data,
                'token': token_data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        

        user = authenticate(request,username=email,password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user) 
            token_data={
                'refresh':str(refresh),
                'access':str(refresh.access_token),
            }

            return Response({
                'msg':'login successful',
                'user':user.name,
                'token':token_data
            }, status=status.HTTP_200_OK)
        return Response({'error':'Invalid email or password'},status = status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self,request):
    

        try:
            refresh_token=request.data.get('refresh')
            if refresh_token is  None:
                return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'msg': 'Logout successful '}, status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
        
    

