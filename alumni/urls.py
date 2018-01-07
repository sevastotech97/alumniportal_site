from django.conf.urls import url
from . import views

urlpatterns = [
    # /alumni/
    url(r'^$', views.index, name='index'),

    # /alumni/712/
    url(r'^(?P<program_id>[0-9]+)/$', views.detail, name='detail'),
]