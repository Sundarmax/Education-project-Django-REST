from rest_framework import serializers
from .models import ques_rules,ques_create

class QuestionRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ques_rules
        fields = '__all__'
class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ques_create
        fields = '__all__'
