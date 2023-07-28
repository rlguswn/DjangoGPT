from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .serializers import UserSerializer, LoginSerializer


class UserRegister(APIView):
    def get(self, request):
        return render(request, 'user/user_register.html')
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid credentials'})


class UserLogin(APIView):
    def get(self, request):
        return render(request, 'user/user_login.html')
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')

        serializer = LoginSerializer(request, request.POST)
        if serializer.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
