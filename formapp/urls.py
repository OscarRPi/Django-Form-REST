# formapp/urls.py

from django.urls import path  

from .views import UserView

urlpatterns = [
    path('',UserView.as_view(),name='users'),
    path('<int:id>',UserView.as_view(),name='users_id'),
]