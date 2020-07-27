
from .models import Images,City

from django import forms
from django.utils import timezone


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__' 


class ImageForm(forms.ModelForm):

    date = forms.DateField(
                widget=forms.DateInput(attrs={
            'class': 'input1',
            'id':'datepicker',
            'placeholder':'Date of Newspaper',
            'label':'Date'
        })
        , required=False)

    class Meta:                             
        model = Images
        fields = '__all__'
