from django.db import models

# Create your models here.
class Mathematics(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=1)
    marks = models.IntegerField(default=0)
    difficulty_level = models.CharField(max_length=1,blank=True)


