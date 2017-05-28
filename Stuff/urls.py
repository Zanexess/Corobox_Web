from django.conf.urls import url
from Stuff import views

urlpatterns = [
    url(r'^stuff/$', views.stuff_list),
    url(r'^stuff_transform/(?P<uuid>[^/]+)/$', views.order_to_stuff),
]