from django import forms 
from .models import *
from datetime import datetime



class AddPostForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = '__all__'
        widgets ={
        'name': forms.TextInput(attrs={'placeholder': "Введите ваше имя"}), 
    }