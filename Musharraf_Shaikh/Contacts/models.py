from django.db import models
from django.utils import timezone


# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    phone_number = models.CharField(max_length=12,null=False,default='+1')
    email = models.EmailField(unique=True)
    notes = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.created_time:
            self.created_time = timezone.now()
        super(Contacts, self).save(*args, **kwargs)