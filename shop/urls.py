from django.conf.urls import url
from shop import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^store/$',  views.StoreList.as_view()),
    url(r'^store/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)