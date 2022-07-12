from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Serial
from .serializers import Serialserializer


@api_view(['GET', 'POST'])
def serial_list(request):
    """
    List all code Serials, or create a new Serial.
    """
    if request.method == 'GET':
        serials = Serial.objects.all()
        serializer = Serialserializer(serials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Serialserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def serial_detail(request, pk):
    """
    Retrieve, update or delete a code Serial.
    """
    try:
        serial = Serial.objects.get(pk=pk)
    except Serial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Serialserializer(serial)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Serialserializer(serial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Serial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)