from django.conf.urls import url
from Order import views

urlpatterns = [
    url(r'^order/$', views.order_get),
    url(r'^order_put/$', views.order_put),
    url(r'^order_del/(?P<uuid>[^/]+)/$', views.order_del),
]