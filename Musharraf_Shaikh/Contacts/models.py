from django.db import models
from django.utils import timezone

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, default="")
    is_done = models.BooleanField(default=False)
    email = models.EmailField()
    created_time = models.DateTimeField(auto_now_add=True, editable=False)