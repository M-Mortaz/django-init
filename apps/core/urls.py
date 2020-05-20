from django.conf.urls import url, include
from apps.core import views
urlpatterns = [
    url(r'^token/$', views.TokenView.as_view(), name='get-token')
]
