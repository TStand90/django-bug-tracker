from django.db import models
from django.contrib.auth.models import User


class Bug(models.Model):
    PRIORITY = (
        ('1', 'Very Low'),
        ('2', 'Low'),
        ('3', 'Medium'),
        ('4', 'High'),
        ('5', 'Very High'),
    )
    STATUS = (
        ('1', 'Open'),
        ('2', 'Closed'),
    )
    title = models.CharField(max_length=250)
    priority = models.CharField(max_length=1, choices=PRIORITY)
    status = models.CharField(max_length=1, choices=STATUS)
    assigned_to = models.ManyToManyField(User, blank=True)
    comments = models.TextField(blank=True)
