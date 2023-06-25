from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    person_name=models.CharField(max_length=70)
    person_pass = models.CharField(max_length=4,validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')])
    cash = models.IntegerField(default=0)

    def __str__(self):
        return self.person_name
class machine(models.Model):
    money_200=models.IntegerField(default=200)
    money_100=models.IntegerField(default=200)
    money_50=models.IntegerField(default=200)
    money_20=models.IntegerField(default=200)
    money_10=models.IntegerField(default=200)
    money=models.IntegerField(default=76000)





