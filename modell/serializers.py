from rest_framework import serializers
from .models import Bio, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio    
        fields = '__all__'
    