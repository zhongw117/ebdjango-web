from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workexperience', views.workexperience, name='workexperience'),
    path('externallink', views.externallink, name='externallink'),
]