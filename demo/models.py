from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Weapon(models.Model):
    power = models.IntegerField()
    rarity = models.CharField(max_length=50)
    value = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


