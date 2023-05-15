from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detectme', views.detectme, name='detectme'),  # views.py에 있는 detectme() 함수 추가
    path('show_sim', views.mediapipeCam.show_sim, name='show_sim')
    # path('origvideo', views.origvideo, name='origvideo'),  # views.py에 있는 detectme() 함수 추가
]