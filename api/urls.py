from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import * 



urlpatterns = [
    url(r'^companies/$', CompanyViewSet),
    url(r'^companies/(?P<pk>[0-9]+)/$', CompanyDetail),
    url(r'^matches/$', MatchViewSet),
    #url(r'^get/$', get),
    url(r'^get/(?P<pk>[0-9]+)/$', get),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
