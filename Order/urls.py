from django.conf.urls import url
from Order import views

urlpatterns = [
    url(r'^order_to/$', views.order_get),
    url(r'^order_to_put/$', views.order_put),
    url(r'^order_to_upd/(?P<uuid>[^/]+)/$', views.order_upd),
    url(r'^order_to_del/(?P<uuid>[^/]+)/$', views.order_del),

    url(r'^order_from/$', views.order_from_get),
    url(r'^order_from_put/$', views.order_from_put),
    url(r'^order_from_del/$', views.order_del),
]