from rest_framework import serializers
from .models import  Twitte


class TwitterSerializer(serializers.ModelSerializer):
    like = serializers.IntegerField(read_only=True)
    class Meta:
        model = Twitte
        fields = ['author','text','created_at','like','id']


class LikeSerializer(serializers.Serializer):
    count = serializers.IntegerField(default=0)