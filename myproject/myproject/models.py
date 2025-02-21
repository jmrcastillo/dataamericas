from django.db import models

# Create your models here.


class Data(models.Model):
    source = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
