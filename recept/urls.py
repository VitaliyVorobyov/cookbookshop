from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('recepts/', views.recepts, name='recepts'),
    path('recepts/<int:pk>/', views.DishView.as_view(), name='dish'),
    path('<int:pk>/newingredient/', views.new_ingredient, name='new_ingredient'),
    path('newdish/', views.new_dish, name='newdish'),
]
