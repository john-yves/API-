from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from .models import Language,Content, Programmer
from .serializers import LanguageSerializer,ContentSerializer,ProgrammerSerializer


class HelloView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'message': 'Hello,World!'}
        return Response(content)

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer 
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Contentview(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class Programmerview(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
