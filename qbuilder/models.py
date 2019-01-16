from django.db import models
# Model For Adding a new question
class ques_create(models.Model):
    IMPORTANCE_SCORE = (
    ('LOW','Low'),
    ('NORMAL', 'Normal'),
    ('HIGH','High'),
    )
    parentid = models.CharField(max_length=250)
    staticid = models.AutoField(primary_key=True)
    qid = models.CharField(max_length=250)
    question = models.TextField()
    a= models.CharField(max_length=250)
    b= models.CharField(max_length=250)
    c= models.CharField(max_length=250)
    d= models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    importance = models.CharField(max_length=6, choices= IMPORTANCE_SCORE, default='LOW')
    complexity = models.PositiveIntegerField(default=0)
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
class ques_rules(models.Model):
    rules_id = models.IntegerField(primary_key=True)
    static_id = models.IntegerField()
    parent_id = models.IntegerField()
    correct_id = models.IntegerField()
    wrong_id = models.IntegerField()
