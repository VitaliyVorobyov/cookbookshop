from django.contrib import admin
from .models import DishModel, ReceptModel


# Register your models here.
@admin.register(DishModel)
class DishModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'dish_name',]
    list_filter = ['dish_name',]


@admin.register(ReceptModel)
class ReceptModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ingredient_name', 'count', 'measure', 'dish',]
    list_filter = ['ingredient_name', 'dish',]
