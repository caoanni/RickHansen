from django.conf.urls import patterns, url
from BarrierBuster import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^createPin/$', views.createPin, name='createPin'),
    url(r'^searchPin/$', views.searchPin, name='searchPin'),
	url(r'^pins/(?P<pin_id>\d+)/$', views.pinDetail, name='pindetail'),
)