from django.db import models

# Create your models here.
# class Profile(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField(max_length=150)
#     password = models.CharField(max_length=150)

#     def __str__(self):
#         return self.username


class TicketModel(models.Model):
    department = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    url = models.URLField(max_length=150)
    description = models.TextField(max_length=1000)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    files = models.FileField(upload_to=None,max_length=140,blank=True)