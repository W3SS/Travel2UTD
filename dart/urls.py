from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^driver$', views.driver, name='driver'),
    url(r'get_location/(?P<bus_id>[0-9]{4})$', views.get_bus_location, name='get_bus_location'),
    url(r'update_location/(?P<bus_id>[0-9]{4})$', views.set_bus_location, name='set_bus_location'),
    url(r'all', views.get_all_bus_location, name='get_all_bus_location'),
    url(r'register', views.register_bus, name='register_bus'),
    url(r'delete_bus/(?P<bus_id>[0-9]{4})$', views.delete_bus, name='delete_bus')
]