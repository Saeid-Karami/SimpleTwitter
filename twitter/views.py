from django.shortcuts import render
from .models import  Twitte
from rest_framework import generics
from .serializers import LikeSerializer, TwitterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


class TwitteViewSet(ModelViewSet):
    queryset = Twitte.objects.all()
    serializer_class = TwitterSerializer


class LikeViewSet(generics.GenericAPIView):
    serializer_class = LikeSerializer
    def post(self,request,*args,**kwargs):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            post = Twitte.objects.get(id=serializer.validated_data['count'])
            post.like += 1
            post.save()
            return Response("Like",status=status.HTTP_200_OK)
    
    