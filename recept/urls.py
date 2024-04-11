from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recepts/', views.ReceptsView.as_view(), name='recepts'),
    path('recepts/<int:pk>/', views.DishView.as_view(), name='dish'),
    path('recepts/newdish/', views.NewDishView.as_view(), name='newdish'),
    path('recepts/<int:pk>/edit/', views.UpdateDishView.as_view(), name='edit_ingredient'),
    path('recepts/<int:pk>/delete_dish', views.DeleteDishView.as_view(), name='delete_dish'),
    path('recepts/<int:pk>/delete_ingredient/', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
]
