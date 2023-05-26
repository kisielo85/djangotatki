from django.db import models
from django.contrib.auth.models import User

class Notatka(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    