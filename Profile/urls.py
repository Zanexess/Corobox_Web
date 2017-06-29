from django.conf.urls import url
from Profile import views

urlpatterns = [
    url(r'^profile/$', views.profile),
    url(r'^profile_upd/(?P<pk>[0-9]+)/$', views.profile_upd)
]