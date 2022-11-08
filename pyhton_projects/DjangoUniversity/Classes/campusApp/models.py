# import database
from django.db import models




# creating a class that will create attributes in database
# we will see it when go to admin page of the project
class UniversityCampus(models.Model):
    Campus_ID = models.IntegerField(default=None, blank=True, null=False)
    Campus_name = models.CharField(max_length=65, default=None, blank=True, null=False)
    State = models.CharField(max_length=2, default='', blank=True, null=False)
# create models manager
    objects = models.Manager()

# creatin method that will return a campus_name in browser admin page
    def __str__(self):
        return self.Campus_name
# removing 's' from admin page University Campuss (remove last 's'
    class Meta:
        verbose_name_plural = "University Campus"






# Create your models here.
