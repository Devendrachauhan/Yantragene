from django.conf.urls import url
from .import views

urlpatterns=[
	url(r'^$',views.branch, name='event'),
	url(r'^details/(?P<id>\d+)/', views.event_detail, name="datail"),
	url(r'^register/$', views.register_view, name="register"),
]