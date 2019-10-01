from django.urls import path
from . import views

urlpatterns =[
    path('',views.promosmsview,name='promosmsview'),
]
