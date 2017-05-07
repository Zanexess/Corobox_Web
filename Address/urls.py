from django.conf.urls import url
from Address import views

urlpatterns = [
    url(r'^address_list/$', views.address_list)
]