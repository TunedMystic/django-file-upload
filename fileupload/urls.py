from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fileupload.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r"^$", TemplateView.as_view(template_name = "default/index.html"), name = "index"),
    url(r"^p/", include("pics.urls", namespace = "pics")),
    
    url(r'^admin/', include(admin.site.urls)),
)
