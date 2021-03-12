from django.contrib.auth.models import AbstractUser
from django.db import models

Gender = (
    ('Male', 'Male'),
    ('Female','Female')
)


class UserModel(AbstractUser):
    school = models.CharField(max_length=50,blank=True, null=True)
    gender = models.CharField(max_length=6, choices=Gender,blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)