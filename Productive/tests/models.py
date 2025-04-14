from django.db import models

# Create your models here.
class TestModel(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=140)
    phone = models.IntegerField(null=True)
    join_date = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
