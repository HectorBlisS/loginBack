from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class UserViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated,]



