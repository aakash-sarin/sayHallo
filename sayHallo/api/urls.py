from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('hallo', views.hallo, name='hallo'),
]