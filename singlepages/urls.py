from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing), #landing()함수 실행
]