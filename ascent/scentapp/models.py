from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_surname=models.CharField(max_length=100)
    contact_email=models.CharField(max_length=100)
    contact_comment=models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField(default=timezone.now)
    message = models.TextField(blank=True, null=True)  # Fusha për mesazhin

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"

class TopNote(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title     
    
