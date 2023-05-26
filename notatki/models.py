from django.db import models
from django.contrib.auth.models import User

class Notatka(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def next(self):
        n=self.__class__.objects.filter(id__gt=self.id).order_by('id').first()
        if n: return n
        return self.__class__.objects.order_by('id').first()
    
    def previous(self):
        n=self.__class__.objects.filter(id__lt=self.id).order_by('-id').first()
        if n: return n
        return self.__class__.objects.order_by('-id').first()
    