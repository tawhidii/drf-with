
from rest_framework import serializers
from watchlists.models import Movies

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self,validated_data):
        return Movies.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.is_active = validated_data.get('is_active')
        instance.save()
        return  instance



    