from django.http import JsonResponse
from.models import Beach
from.serializers import BeachSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics




@api_view(['GET'])
def beach_list(request, format=None):
  #get all drinks
  #serialize them
  #return json
  
  if request.method == 'GET':
      beach = Beach.objects.all()
      serializer = BeachSerializer(beach, many=True) #this will serialise all of them
      return Response(serializer.data)
 
  # if request.method == 'POST':
  #   serializer = BeachSerializer(data=request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response (serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT', 'DELETE'])
def beach_detail(request, id, format=None):
  
  try: 
    drink = Beach.objects.get(pk=id)
  except Beach.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
    
  if request.method == 'GET':
     serializer = BeachSerializer(drink)
     return Response(serializer.data)
  elif request.method == 'PUT':
     serializer = BeachSerializer(drink, data=request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
     drink.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
   
   
   
class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
   
   
   
   