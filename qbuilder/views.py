from django.shortcuts import render
#rest_framework
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
#model 
from .models import ques_rules,ques_create
#serializer
from .serializers import QuestionRulesSerializer,QuestionCreateSerializer
# json
import json
#Return the set of questions 
@api_view(['GET', 'POST','DELETE'])
def ques_ListAll(request):
    if request.method == 'GET':
        data = ques_create.objects.all()
        serializer = QuestionCreateSerializer(data,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionCreateSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data = ques_create.objects.all()
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)                   
#Return the Question by Given id.
@api_view(['GET','PUT','DELETE'])
def ques_List(request,pk):
    try:
        data = ques_create.objects.get(staticid = pk)
    except ques_create.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = QuestionCreateSerializer(data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = QuestionCreateSerializer(data, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#Return the set of sub questions by Given ID


#Return the rules for all question
@api_view(['GET', 'POST'])
def rules_ListAll(request):
    if request.method == 'GET':
        data = ques_rules.objects.all()
        serializers = QuestionRulesSerializer(data,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = QuestionRulesSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Return the rules by given id
@api_view(['GET','PUT','DELETE'])
def rules_List(request,pk):
    try:
        data = ques_rules.objects.get(rules_id = pk)
    except ques_rules.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = QuestionRulesSerializer(data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = QuestionRulesSerializer(data, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
