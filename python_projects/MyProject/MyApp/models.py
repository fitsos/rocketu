from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=20)
	joined = models.DateField()