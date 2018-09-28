from django.shortcuts import render
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def home(request):
	return render(request, 'app/home.html')

def login(request):
	return render(request, 'app/login.html')

def user(request, key):
	token = Token.objects.get(key=key)
	user = token.user
	serializer = UserSerializer(user, many=False)
	return JsonResponse(serializer.data, safe=False)
