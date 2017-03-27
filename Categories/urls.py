from django.conf.urls import url
from Categories import views

urlpatterns = [
    url(r'^categories/$', views.categories_list),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.category_detail),
]