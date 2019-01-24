from django.shortcuts import render
#rest_framework
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
#model 
from .models import create_rules,ques_create,create_topic
from django.contrib.auth.models import User
#serializer
from .serializers import QuestionRulesSerializer,QuestionCreateSerializer,QuestionTopicSerializer,UserSerializer
# json
import json
from django.http import QueryDict
import os 
#File Processing 
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'qid.txt')
file_pathR = os.path.join(module_dir, 'rid.txt')
file_pathQ = os.path.join(module_dir, 'publicid.txt')
#Static id Generation
def write(number,qid):
    if qid == 1:
        with open(file_path, 'w') as f:
            f.write('%d' % number)
            f.close()
    if qid == 2:
        with open(file_pathR, 'w') as f:
            f.write('%d' % number)
            f.close()
    if qid == 3:
        with open(file_pathQ, 'w') as f:
            f.write('%d' % number)
            f.close()
def read(qid):
    if qid == 1:
        f = open(file_path, 'r')   
    if qid == 2:
        f = open(file_pathR, 'r')
    if qid == 3:
        f = open(file_pathQ, 'r')
    text = f.readline()
    id =  int(text)
    id =  id + 1
    write(id,qid)
    f.close()
    return id
# Validate User Login 
@api_view(["GET","POST"])
def login(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
        login_user = UserSerializer(user).data
        result = {'id':login_user['id'], 'username':login_user['username']}
        return Response(result)
        '''return Response({'token': token.key},
                    status=HTTP_200_OK)'''
#Create a new user
@api_view(['POST'])
def create_User(request):
    if request.method == 'POST':
            data = request.data
            serializer = UserSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#Return the set of questions 
def SquarebracketFilter(new_dict):
    for key,value in new_dict.items():
        result = str(value).replace('[','').replace(']','')
        new_dict[key]=result
@api_view(['GET', 'POST','DELETE'])
def ques_ListAll(request):
    if request.method == 'GET':
        data = ques_create.objects.all()
        serializer = QuestionCreateSerializer(data,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = dict(request.data)
        sid = read(1)
        data.update({'staticid':sid})
        public_id = read(3)
        if int(data['parentid']) == 0:
            public_id = "MN_"+str(public_id)
            data.update({'qid':public_id})
        else:
            public_id = "SB_"+str(public_id)
            data.update({'qid':public_id})
        SquarebracketFilter(data) 
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        serializer = QuestionCreateSerializer(data = qdict)
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
@api_view(['GET'])
def subques_list(request,pk):
    try:
            data = {}
            data['subquestions']=[]
            i = 0
            for res in ques_create.objects.filter(parentid =pk):
                data['subquestions'].append({"staticid":res.staticid,"qid":res.qid})
                #data.update({"staticid":res.staticid,"qid":res.qid}) 
            result = json.dumps(data)             
            return Response(json.loads(result))
    except ques_create.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
#Return the set of Main questions by Given ID
@api_view(['GET'])
def mainques_list(request,pk):
    try:
            data = {}
            data['mainquestions']=[]
            i = 0
            for res in ques_create.objects.filter(parentid = 0):
                if res.staticid != int(pk):
                    data['mainquestions'].append({"staticid":res.staticid,"qid":res.qid}) 
            result = json.dumps(data)             
            return Response(json.loads(result))
    except ques_create.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
#Return the rules for all question
@api_view(['GET', 'POST','DELETE'])
def rules_ListAll(request):
    if request.method == 'GET':
        data = create_rules.objects.all()
        serializers = QuestionRulesSerializer(data,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = dict(request.data)
        rid = read(2) 
        data.update({'rules_id':rid})
        static_id = data['static_id']
        print(static_id)
        SquarebracketFilter(data) 
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        print(qdict)
        serializer = QuestionRulesSerializer(data = qdict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data = create_rules.objects.all()
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)       
#Return the rules by given id
@api_view(['GET','PUT','DELETE'])
def rules_List(request,pk):
    try:
        data = create_rules.objects.get(static_id = pk)
    except create_rules.DoesNotExist:
        return Response("404",status = status.HTTP_200_OK)
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

#Return the set of Main Topics 
@api_view(['GET', 'POST'])
def topic_main(request):
    if request.method == 'GET':
        data = create_topic.objects.all()
        serializers = QuestionTopicSerializer(data,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = QuestionTopicSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#Return the Main Topic by Given id 
@api_view(['GET','PUT','DELETE'])
def topic_mainList(request,pk):
    try:
        data = create_topic.objects.get(static_id = pk)
    except create_topic.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = QuestionTopicSerializer(data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = QuestionTopicSerializer(data, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

