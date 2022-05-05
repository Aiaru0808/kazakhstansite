from django.db import models

# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField('Аты', max_length=50)
    surname = models.CharField('Фамилиясы', max_length=50)
    email = models.EmailField('Электрондық почта', max_length=50)
    city = models.CharField('Қала', max_length=50)
    mobile_number = models.IntegerField('Mобилдік нөмері')

    def __str__(self):
        return self.username
