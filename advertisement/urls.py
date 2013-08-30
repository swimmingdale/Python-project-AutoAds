from django.conf.urls import patterns, url
from AutoAds import settings

from advertisement import views

urlpatterns = patterns('',
                       url(r'^home', views.home, name='home'),
                       url(r'^search', views.search, name='search'),
                       url(r'^results', views.search, name='results'),
                       url(r'^add', views.add, name='add'),
                       url(r'^added', views.add, name='added'),
                       url(r'^(?P<car_id>\d+)/$', views.detail, name='detail'),
                      )
