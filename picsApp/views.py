from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.conf import settings

from picsApp.models import PictureUpload
from picsApp.forms import PictureUploadForm
from picsApp.dirDetails import dirFileDetails

# Create your views here.
def uploadFile(request):
  """
  Displays an upload form.
  """
   
  # If a form was POSTed.
  if request.method == "POST":
    # Instantiate a ModelForm with the request data.
    uploadForm = PictureUploadForm(request.POST, request.FILES)
    if uploadForm.is_valid():
      # Save the form data (the picture).
      uploadForm.save()
      return HttpResponseRedirect(reverse("index"))
  # No form data, so return an empty form.
  else:
    uploadForm = PictureUploadForm()
  return render(request, "picsApp/uploadForm.html", {"form": uploadForm})


def listFiles(request):
  """
  Displays a list of all uploaded images.
  """
   
  # Get a the details of each uploaded file as a list.
  fileDetails = dirFileDetails(settings.MEDIA_ROOT)
  return render(request, "picsApp/uploadList.html", {"files": fileDetails})