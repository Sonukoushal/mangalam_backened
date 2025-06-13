from rest_framework.views import APIView  # GET, POST, PUT, DELETE jaise methods define kar sakte ho
from rest_framework.response import Response 
from rest_framework import status  #status DRF ka module hai jisme predefined HTTP response codes diye hote hain.
from .serializers import UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import UserManager , CustomUser

class SignupView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save() 

             # JWT Token Generate karo
            refresh = RefreshToken.for_user(user)
            token_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({
                'msg': 'Signup successful ✅',
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

            return Response({'msg': 'Logout successful ✅'}, status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

