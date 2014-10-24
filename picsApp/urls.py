from django.conf.urls import patterns, include, url

from picsApp import views

urlpatterns = patterns('',
   
   
  url(r"^uploadfile/$", views.uploadFile, name = "upload-files"),
  url(r"^listfiles/$", views.listFiles, name = "list-files")
  
)