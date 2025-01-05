from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id', 'title', 'description', 'completed', 
            'priority', 'status', 'due_date', 'assigned_to',
            'created_by', 'project', 'tags', 'created_at', 
            'updated_at', 'completed_at'
        ]