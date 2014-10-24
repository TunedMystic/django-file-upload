from django import forms
from django.utils.translation import ugettext_lazy as _

from pics.models import PictureUpload

class PictureUploadForm(forms.ModelForm):
   
  class Meta:
    model = PictureUpload
    exclude = []
    labels = {
      "img": _("Image")
    }