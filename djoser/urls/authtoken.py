from django.conf.urls import url

from djoser import views


urlpatterns = [
    url(r'^token/create/$', views.TokenCreateView.as_view(), name='login'),
    url(r'^token/destroy/$', views.TokenDestroyView.as_view(), name='logout'),
]
