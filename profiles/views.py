from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission

from profiles.models import User
from profiles.permissions import IsOwnerOrReadOnly
from profiles.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.template import loader

from django.http import HttpResponse

@api_view(['GET'])
def api_root(request, format=None):
    return HttpResponse({
        # 'users': reverse('user-list', request=request, format=format),
        #render(request, 'index.html')
        loader.get_template('index.html').render()
    })