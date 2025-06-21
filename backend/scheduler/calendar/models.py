from django.db import models

# Create your models here.

class Calendar(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    