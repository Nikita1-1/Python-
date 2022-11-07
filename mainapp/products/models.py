from django.db import models

#creating choices for where people can select only this types on the websites
TYPE_CHOICES = [
    ("appetizers","appetizers"),
    ("entrees","entrees"),
    ("drinks", "drinks"),
    ("desert", "desert"),
]



class Product(models.Model): #inherit fom the class models.Model
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default='', blank=True, null=False)# basicaly its is name with no more than 60 char, default value-empty)
    description = models.TextField(max_length=300, default='', blank=True)
    price = models.DecimalField(default = 0.00, max_digits = 10000, decimal_places = 2)
    image = models.CharField(max_length = 255, default='', blank=True)

    objects = models.Manager()

    def __str__(self): # changes a name of the product that we created.
        return self.name