from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('done/<int:id>/', views.done, name='done'),
    path('undone/<int:id>/', views.undone, name='undone'),
    path('update/<int:id>/', views.update, name='update'),
]
