from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_people = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} : {self.price}"