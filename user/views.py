from rest_framework import generics, status
from user import serializers
from user.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

def set_token(user, message):
    refresh_token = RefreshToken.for_user(user)
    response = Response({'access_token': str(refresh_token.access_token)}, message)
    response.set_cookie(
        key='refresh',
        value=str(refresh_token),
        httponly=True,
        samesite='Strict',
        secure=True,
        max_age=3600
    )
    return response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)
        if user.is_authenticated:
            response = set_token(user, 201)
            return response
        else: 
            raise AuthenticationFailed(status=status.HTTP_401_UNAUTHORIZED)

class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            user.save()
            return Response({"message": "Foydalanuvchi tizimga kirishi muvaffaqiyatli amalga oshirildi"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Username yoki parol noto'g'ri"}, status=400)

class LogoutView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.LoginSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Foydalanuvchi tizimdan muvaffaqiyatli chiqarildi"}, status=status.HTTP_200_OK)