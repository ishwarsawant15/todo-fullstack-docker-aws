# backend/api/serializers.py

from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    
    Theory:
    - Serializers convert complex data types (Django models) to JSON
    - ModelSerializer automatically creates fields based on model
    - fields: Specifies which fields to include
    - read_only_fields: Fields that cannot be modified via API
    """
    
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']