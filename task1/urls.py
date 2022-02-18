from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.formView, name='form'),
    path('succes/', views.success, name='succes'),
    path('detail/', views.userDetail, name='detail'),

]
