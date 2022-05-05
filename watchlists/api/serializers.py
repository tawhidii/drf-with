
from turtle import title
from wsgiref.validate import validator
from rest_framework import serializers
from watchlists.models import Movies

# using validators 
def title_validate(value):
    if len(value) < 2:
        raise serializers.ValidationError('Title is too short !!')
    return value



class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(validators=[title_validate])
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

    # Example of field level validation .... 
    # def validate_title(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('title is too short !!')
    #     return value

    # Object level validation
    def validate(self,data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('title and description can''t be same ')
        else:
            return data


    