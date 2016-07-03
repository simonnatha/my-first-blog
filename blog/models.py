from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

        
class formulaireinscription(models.Model):
    """docstring forformulaired'inscription models.Model"""
    pseudo = models.CharField(max_length= 30)
    mail = models.CharField(max_length = 50)
    mdp = models.CharField(max_length = 30)
    cmdp =models.CharField(max_length = 30)

    def __str__(self):
        return self.pseudo
