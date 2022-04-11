import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=512)
    created_at = models.DateTimeField("date created")
    translation = models.CharField(max_length=512)
    points = models.IntegerField(default=0)
    example_sentence = models.TextField()
    last_training = models.DateTimeField("date last trained")


    def was_trained_recently(self):
        return self.last_training >= timezone.now() - datetime.timedelta(days=7)


