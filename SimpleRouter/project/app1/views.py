from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .Serializers import BlogModelSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
# Create your views here.

class BLogViewsetAPI(viewsets.ViewSet):
    
    def create(self,request):
        serializer=BlogModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        obj=Blog.objects.all()
        serializer=BlogModelSerializer(obj,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Blog,pk=pk)
        serializer=BlogModelSerializer(obj)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Blog,pk=pk)
        serializer=BlogModelSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Blog,pk=pk)
        serializer=BlogModelSerializer(data=request.data,instance=obj,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Blog,pk=pk)
        obj.delete()
        return Response(data={'data deleted'},status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    
    
    
    
    
    
    
    