from django.shortcuts import render
from django.http import HttpResponse

from pics.forms import PictureUploadForm

# Create your views here.
def uploadFile(request):
  return HttpResponse("This is the uploads page.")


def listFiles(request):
  return HttpResponse("This is the list files page.")