from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    # image -> imagefile 변경 
    class Meta:
        model = Photo
        fields = ('title','author' ,
        'imagefile',
        'description','price') 