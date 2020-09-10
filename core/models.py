from django.db import models
from django.shortcuts import reverse 

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class TreeMain(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tree:detail", kwargs={'pk': self.pk})