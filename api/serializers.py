from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    class Meta:
        model = Person
        fields = ('id', 'name', 'created_at', 'updated_at')

