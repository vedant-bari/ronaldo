
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')

