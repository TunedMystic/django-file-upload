"""
    Amtex Training Project
    "Image Upload Program"
       
      Sandeep Jadoonanan
       October 24, 2014
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from picsApp.models import PictureUpload

class PictureUploadForm(forms.ModelForm):
   
  class Meta:
    model = PictureUpload
    exclude = []
    labels = {
      "img": _("Image")
    }