from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from  ..serializers.serializer import RegisterationUserSerializer,LoginUserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from ..models import CustomUser
from rest_framework.permissions import AllowAny,IsAuthenticated




class RegisterView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=RegisterationUserSerializer


class Loginview(generics.CreateAPIView):
    serializer_class=LoginUserSerializer
    permission_classes=[AllowAny]

    def post(self,request):
        username=request.get.data('username')
        password=request.get.data('password')




        if not username or not password:
            return Response({'error':'username and password are required'},status=400)
        
        user=authenticate(username=username ,password=password)
        if user is None:
            return Response({'erro':'Invalid credentials'},status=401)
        
        refresh=RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'role': user.role,
            }
        })





