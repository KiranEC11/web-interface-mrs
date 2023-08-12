from django.urls import path
from . import views


urlpatterns=[
    path("", views.TitleView, name= "enter_title"),
    path("recommendations/", views.TitleView, name='recommendations'),
    
]