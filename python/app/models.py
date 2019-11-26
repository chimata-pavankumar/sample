from django.db import models

# Create your models here.
class marks(models.Model):
    ENG = models.IntegerField()
    MAT = models.IntegerField()
    SCI = models.IntegerField()
    PERCENTAGE = models.IntegerField()

class insurence(models.Model):
    NAME = models.CharField(max_length=30)
    DATE = models.DateField()

class age(models.Model):
    DATE = models.DateField()
