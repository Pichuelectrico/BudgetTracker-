from django.db import models

# Create your models here.
class Person(models.Model):
    person_user = models.CharField(max_length=64)
    pub_date = models.DateTimeField("Date created")
    name = models.CharField(max_length=30)
    password = models.CharField(Max_lenght=64)

class Total_Money(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=5, decimal_places=2)
    commmit_date = models.DateTimeField("Change Date")

class Fixed_bills(models.Model):
    more_moneysss = models.ForeignKey(Total_Money, on_delete=models.CASCADE)
    bill_text = models.CharField(max_length=120)
    money = models.DecimalField(max_digits=5, decimal_places=2)

class Variable_bills(models.Model):
    money = models.ForeignKey(Total_Money, on_delete=models.CASCADE)
    bill_text = models.CharField(max_length=200)
    money = models.DecimalField(max_length=5, decimal_places=2)