from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from shop_api import views

urlpatterns = [
    url(r'^store/$', views.StoreList.as_view()),
    url(r'^store/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^docitem/$', views.DocItemList.as_view()),
    url(r'^docitem/(?P<pk>[0-9]+)/$', views.DocItemDetail.as_view()),
    url(r'^doctype/$', views.DocumentTypeList.as_view()),
    url(r'^doctype/(?P<pk>[0-9]+)/$', views.DocumentTypeDetail.as_view()),
    url(r'^document/$', views.DocumentList.as_view()),
    url(r'^document/(?P<pk>[0-9]+)/$', views.DocumentDetail.as_view()),
    url(r'^product/$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^unit/$', views.UnitTypeList.as_view()),
    url(r'^unit/(?P<pk>[0-9]+)/$', views.UnitTypeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
