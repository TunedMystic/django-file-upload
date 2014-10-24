"""
    Amtex Training Project
    "Image Upload Program"
       
      Sandeep Jadoonanan
       October 24, 2014
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fileupload.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r"^$", TemplateView.as_view(template_name = "default/index.html"), name = "index"),
    url(r"^p/", include("picsApp.urls", namespace = "pics")),
    
    #url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
  urlpatterns += patterns('',
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  )