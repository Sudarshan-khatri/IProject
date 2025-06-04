from django.urls import path
from .viewsets.viewset import RegisterView,Loginview


urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',Loginview.as_view(),name='login'),
]
