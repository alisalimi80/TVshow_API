from .models import Cast
from .models import Serial
from .models import Genre
from .models import Image

from rest_framework import serializers

class Serialserializer(serializers.ModelSerializer):
    
    casts = serializers.StringRelatedField(many=True) 
    image =  serializers.SlugRelatedField(many=True,slug_field='img',read_only=True) 
    genre= serializers.StringRelatedField(many=True)

    class Meta:
        model = Serial
        fields = ('id', 'name', 'imdb', 'genre','description','publishdate','country','director','casts','image')

        