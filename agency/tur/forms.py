from django import forms
from django.conf import settings
from .models import City, tour
User = settings.AUTH_USER_MODEL

class NewCityCreationForm(forms.ModelForm):
    name = forms.CharField(label='Назва')
    photo = forms.ImageField(label='Фотографія')
    body = forms.CharField(label='Опис', widget=forms.Textarea())

    # required_css_class = "field"
    # error_css_class = "error"

    class Meta:
        model = City
        fields = ('name', 'photo', 'body')

# class UpdateForm(forms.ModelForm):
#     class Meta:
#         model = tour
#         fields = '__all__'