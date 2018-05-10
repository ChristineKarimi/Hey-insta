from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views


urlpatterns =[
  url(r'^$', views.index, name='Home'),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),

]
