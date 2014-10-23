from django import forms

from pics.models import PictureUpload

class PictureUploadForm(forms.ModelForm):
   
  class Meta:
    model = PictureUpload