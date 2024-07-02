from django.db import models
import datetime

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200, default='John')
    reservation_date = models.DateField(default=datetime.date.today)
    reservation_slot = models.SmallIntegerField(default=10)
    number_of_guests = models.SmallIntegerField(default=1)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200, default='name') 
   price = models.DecimalField(max_digits=6, decimal_places=2) 
   menu_item_description = models.TextField(max_length=1000, default='') 
   inventory = models.SmallIntegerField(default=1)
   

   #use this for testing...
   def get_item(self):
        return f'{self.name} : {str(self.price)}'
   
   def __str__(self):
       return f"{self.name} : {str(self.price)}"