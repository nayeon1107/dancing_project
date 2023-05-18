from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('stgame', views.stgame, name='stgame'),
    path('rank', views.rank, name='rank'),
    path('detectme', views.detectme, name='detectme'),  # views.py에 있는 detectme() 함수 추가
    path('check_sim', views.check_sim, name='check_sim'),
    # path('origvideo', views.origvideo, name='origvideo'),  # views.py에 있는 detectme() 함수 추가
]