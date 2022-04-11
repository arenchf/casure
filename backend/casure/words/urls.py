from django.urls import path

from . import views

app_name = 'words'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:word_id>/', views.detail, name='detail'),
    path('<int:word_id>/results/', views.results, name='results'),
]