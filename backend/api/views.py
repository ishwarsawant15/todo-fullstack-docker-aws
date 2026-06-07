# backend/api/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer


@api_view(['GET', 'POST'])
def message_list(request):
    """
    API endpoint for listing and creating messages.
    
    GET: Returns all messages
    POST: Creates a new message
    
    Theory:
    - @api_view: Decorator that defines allowed HTTP methods
    - request.method: The HTTP method used
    - request.data: Parsed request body (JSON)
    - Response: Returns JSON response
    - status: HTTP status codes (200, 201, 400, etc.)
    """
    
    if request.method == 'GET':
        # Get all messages from database
        messages = Message.objects.all()
        # Convert to JSON
        serializer = MessageSerializer(messages, many=True)
        # Return JSON response
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Parse incoming JSON data
        serializer = MessageSerializer(data=request.data)
        
        # Validate data
        if serializer.is_valid():
            # Save to database
            serializer.save()
            # Return created object with 201 status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return errors with 400 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint.
    Used by Docker and load balancers to verify service is running.
    """
    return Response({
        'status': 'healthy',
        'message': 'Django API is running!'
    })