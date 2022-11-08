from django.forms import ModelForm
from .models import Product


class productForm(ModelForm):
    class Meta:
        model= Product
        fields = '__all__'