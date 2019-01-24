from rest_framework import serializers
from .models import create_rules,ques_create,create_topic
from django.contrib.auth.models import User
class QuestionRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = create_rules
        fields = '__all__'
class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ques_create
        fields = '__all__'
class QuestionTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = create_topic
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
