from django.db import models

class ClientMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)