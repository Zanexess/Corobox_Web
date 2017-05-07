from django.conf.urls import url
from Address import views

urlpatterns = [
    url(r'^address/$', views.address_get),
    url(r'^address_del/(?P<pk>[0-9]+)/$', views.address_del),
    url(r'^address_put/$', views.address_put),
    url(r'^address_upd/(?P<pk>[0-9]+)/$', views.address_upd),
]