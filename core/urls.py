from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [

    path('music/<int:pk>', views.MusicView.as_view()),
    path('musics', views.MusicsList.as_view()),

]
