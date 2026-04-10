import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    put_date=models.DateTimeField("Date of Published question")

    def __str__(self):
        return self.question_text

    def last(self):
        return self.put_date>=timezone.now()-datetime.timedelta(days=1)

class Vote(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="choices")
    choice=models.CharField(max_length=100)
    vote=models.IntegerField(default=0)

    def __str__(self):
        return self.choice
