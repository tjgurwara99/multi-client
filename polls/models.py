from django.db import models

# Create your models here.


class Question(models.Model):
    """Question Model."""

    question = models.CharField(max_length=256)
    publish_date = models.DateTimeField("date published")


class Choice(models.Model):
    """Choice model."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
