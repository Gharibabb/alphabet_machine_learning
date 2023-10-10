from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-data/', views.add_data_get, name='add_data_get'),
    path('add-data/', views.add_data_post, name='add_data_post'),
    path('practice/', views.practice_get, name='practice_get'),
    path('practice/', views.practice_post, name='practice_post'),
]
