from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('recepts/', views.recepts, name='recepts'),
    path('recepts/<int:pk>/', views.DishView.as_view(), name='dish'),
    path('recepts/<int:pk>/newingredient/', views.new_ingredient, name='new_ingredient'),
    path('recepts/newdish/', views.new_dish, name='newdish'),
]
