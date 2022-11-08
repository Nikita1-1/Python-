from django.contrib import admin
from .models import UniversityCampus

# import our UniversityCampus from models to let admin know that it is existing
# (for connection)

admin.site.register(UniversityCampus)
# Register your models here.
