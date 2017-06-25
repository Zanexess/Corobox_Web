from django.conf.urls import url
from Profile import views

urlpatterns = [
    url(r'^profile/$', views.profile)
]