from django.db import models
# Create your models here.

class Todo(models.Model): #creates table ToDo
    content = models.TextField() #creates column named content
