from django.db import models

# Create your models here.

class Note(models.Model) :
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) # auto_now -> whenever we save a data into our database then it saves its timestamp along with it
    created = models.DateTimeField(auto_now_add=True) # auto_now_add -> create time stamp only once at the creation of the note


    # only display first 50 characters of the string
    def __str__(self):
        return self.body[0:50]