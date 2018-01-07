from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^alumni/', include('alumni.urls')),
    url(r'^admin/', admin.site.urls),
]
