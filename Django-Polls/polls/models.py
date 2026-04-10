from django.db import models

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    put_date=models.DateTimeField("Date of Published question")

class Vote(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=100)
    vote=models.IntegerField(default=0)

