from django.conf.urls import url, include
from profiles import views


urlpatterns = [
    url(r'^$', views.api_root)
]

