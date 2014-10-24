import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from picsApp.models import PictureUpload
from picsApp.forms import PictureUploadForm
from picsApp.simpleFileSize import getSize

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
  limitResults = 12 
  details = []
  for pic in PictureUpload.objects.all()[:limitResults]:
    n = {}
    n["fileName"] = os.path.basename(pic.img.name)
    n["fileExtension"] = os.path.splitext(pic.img.name)[-1]
    n["fileSize"] = getSize(pic.img.size)
    n["fileUrl"] = pic.img.name
    details.append(n)
   
  return render(request, "picsApp/uploadList.html", {"files": details})
