from django.db import models




class UniversityClasses(models.Model):
    title = models.CharField(max_length=68, default="", blank=True, null=False)
    course_number = models.IntegerField(default='', blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default='', blank=True, null=False)
    duration = models.FloatField(default=None, blank=True, null=False)


    # creates model manager
    object = models.Manager()


    #Displays the object output value in the form of a string

    def __str__(self):
        """returns the input value of the title and instructor name"""
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)


#class Meta creates meta data for the UniversityClasses model.
#Django will automatically append the letter ‘s’ to any model name
#meaning the UniversityClasses model would be displayed as
#UniversityClasses. verbose_name_plural allows you to set the exact
#text you would like displayed in the browser
#and removes the plural form of the model name.


    # Removes added 's' that Django adds in the model name in the browser
    class Meta:
        verbose_name_plural = "University Classes"



# Create your models here.
