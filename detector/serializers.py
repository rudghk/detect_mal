from .models import Black
from rest_framework import serializers

class BlackSerializer(serializers.HyperlinkedModelSerializer) : 
    class Meta : 
        model = Black
        fields = ['black_id', 'url']
