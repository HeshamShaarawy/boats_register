from django.db import models
from django.db.models.fields import IntegerField
from datetime import date
from django.urls import reverse

# Create your models here.
GEAR = (
    ('F', 'Fire Fighting Equipment'),
    ('L', 'First Aid and life saving gear')
)

class Owner(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('owners_detail', kwargs={'pk': self.id})

class Boat(models.Model):
    name= models.CharField(max_length=100)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=100)
    comments = models.TextField()
    owners = models.ManyToManyField(Owner)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'boat_id': self.id})
    

class Gear(models.Model):
    item = models.CharField(
        max_length=1,
        choices=GEAR
    )
    quantity = IntegerField(default=1)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    def __str__(self):
        return f"inventory checked of {self.get_item_display()}" 
    
