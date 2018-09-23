from django.urls import path
from . import views

urlpatterns = [
    path('',views.msg_api,name='msg_api'),
]
