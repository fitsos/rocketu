from django.db import models

# Create your models here.
class CarChoice(models.Model):
    make=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    instock=models.BooleanField(default=True)
    description=models.CharField(max_length=255)
    # equipment = models.ManyToManyField('self')
    # CAR_TYPES = (
    #     ('S', 'Sedan' ),
    #     ('T', 'Truck' ),
    #     ('C','Convertible'),
    #     ('U', 'SUV'),
    #     ('V','Van'),
    #     ('P', 'Performance'),
    # )

# class Equipment(models.Model):
#     name=models.CharField(max_length=255)
#     available=models.BooleanField(default=False)
#     CarChoice = models.ManyToManyField('self')