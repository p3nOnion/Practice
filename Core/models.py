from django.db import models
from User.models import User

# Create your models here.

class Writing(models.Model):
    STATUS_CHOICES = (
        (1, 'Part 1'),
        (2, 'Part 2'),
        (3, 'Part 3'),
        (4, 'Part 4'),
    )
    id = models.fields.IntegerField(primary_key=True, auto_created=True, unique=True)
    type = models.IntegerField(choices=STATUS_CHOICES)
    problem = models.TextField(blank=False, default="")
    solution = models.TextField(blank=False, default="")
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.problem

class Speaking(models.Model):
    STATUS_CHOICES = (
        (1, 'Part 1'),
        (2, 'Part 2'),
        (3, 'Part 3'),
        (4, 'Part 4'),
    )
    id = models.fields.IntegerField(primary_key=True, auto_created=True, unique=True)
    type = models.IntegerField(choices=STATUS_CHOICES)
    problem = models.TextField(blank=False, default="")
    solution = models.TextField(blank=False, default="")
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.problem

class PracticeS(models.Model):
    id = models.fields.IntegerField(primary_key=True, auto_created=True, unique=True)
    problem=models.ForeignKey(Speaking, on_delete=models.CASCADE, default=1)
    solution = models.TextField(blank=False, default="")
    user =  models.IntegerField(default=0)

class PracticeW(models.Model):
    id = models.fields.IntegerField(primary_key=True, auto_created=True, unique=True)
    problem=models.ForeignKey(Writing, on_delete=models.CASCADE, default=1)
    solution = models.TextField(blank=False, default="")
    user =  models.IntegerField(default=0)