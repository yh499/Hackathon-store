from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    # url(r'^process$', views.process),
    url(r'^confirm$',views.confirm),
    url(r'^checkout$',views.checkout),
    url(r'^result$', views.result),

    url(r'^product/iphone6$', views.iphone6),
    url(r'^product/iphone6plus$', views.iphone6plus),
    url(r'^product/iphone6s$', views.iphone6s),
    url(r'^product/iphone7$', views.iphone7),
    url(r'^product/iphone7plus$', views.iphone7plus),
    url(r'^product/iphone6splus$', views.iphone6splus),
    # url(r'^cart$', views.cart),

]