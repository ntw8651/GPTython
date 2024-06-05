from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    content = models.TextField()
    create_date = models.IntegerField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class Conversation(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)