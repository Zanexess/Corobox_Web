from django.conf.urls import url
from HomePage.views import HomePage

urlpatterns = [
    url(r'^', HomePage.as_view(), name='home')
]