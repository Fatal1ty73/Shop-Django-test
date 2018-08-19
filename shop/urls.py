from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^store/$', views.store_list),
    url(r'^store/(?P<pk>[0-9]+)/$', views.store_detail),
]