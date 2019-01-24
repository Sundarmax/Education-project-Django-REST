from django.db import models
# Model For Adding a new question
class ques_create(models.Model):
    parentid = models.CharField(max_length=250)
    staticid = models.IntegerField(primary_key=True)
    qid = models.CharField(max_length=250)
    question = models.TextField()
    a= models.CharField(max_length=250)
    b= models.CharField(max_length=250)
    c= models.CharField(max_length=250)
    d= models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    importance = models.CharField(max_length=6)
    complexity = models.TextField(max_length=6)
    time = models.CharField(max_length=200)
    marks = models.CharField(max_length=200)
    foundation = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    core = models.CharField(max_length=250)
    exam = models.CharField(max_length=250)
    fscore = models.CharField(max_length=250)
    sscore = models.CharField(max_length=250)
    cscore = models.CharField(max_length=250)
    escore = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
# Model For Storing Question Ruels
class create_rules(models.Model):
    rules_id = models.CharField(max_length=8)
    static_id = models.CharField(max_length=8)
    parent_id = models.CharField(max_length=8)
    correct_id = models.CharField(max_length=8)
    wrong_id = models.CharField(max_length=8)
# Model for Main Topics
class create_topic(models.Model):
    static_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    main_id = models.IntegerField()
    topic_name = models.CharField(max_length=250)
    count_subtopic = models.IntegerField()
    count_ques = models.IntegerField()
    importance = models.CharField(max_length=100)
    complexity = models.CharField(max_length=100)
    prerequisite = models.CharField(max_length=250)




