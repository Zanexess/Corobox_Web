from django.conf.urls import url
from Order import views

urlpatterns = [
    url(r'^order_to/$', views.order_get),
    url(r'^order_to/(?P<type>[^/]+)$', views.order_get),
    url(r'^order_to_put/$', views.order_put),
    url(r'^order_to_upd/(?P<uuid>[^/]+)/$', views.order_upd),
    url(r'^order_to_del/(?P<uuid>[^/]+)/$', views.order_to_del),
    url(r'^order_to_cancel/(?P<uuid>[^/]+)/$', views.order_to_cancel),
    url(r'^order_to_deliver/$', views.order_to_deliver),
    url(r'^order_to_change_status/$', views.order_to_change_status),


    url(r'^order_from/$', views.order_from_get),
    url(r'^order_from/(?P<type>[^/]+)$', views.order_get),
    url(r'^order_from_put/$', views.order_from_put),
    url(r'^order_from_del/(?P<uuid>[^/]+)/$', views.order_from_del),
    url(r'^order_from_cancel/(?P<uuid>[^/]+)/$', views.order_from_cancel),
    url(r'^order_from_deliver/$', views.order_from_deliver),
    url(r'^order_from_change_status/$', views.order_from_change_status),
]