# backend/api/models.py

from django.db import models


class Message(models.Model):
    """
    Simple model with one field to store messages.
    
    Theory:
    - models.Model: Base class for all Django models
    - CharField: String field with max length
    - DateTimeField: Stores date and time
    - auto_now_add: Automatically set when object is created
    """
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Newest first

    def __str__(self):
        return f"Message {self.id}: {self.content[:30]}..."