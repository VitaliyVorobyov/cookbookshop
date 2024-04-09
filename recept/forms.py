from .models import ReceptModel, DishModel
from django.forms import ModelForm, TextInput, Select, NumberInput


class DishForm(ModelForm):
    class Meta:
        model = DishModel
        fields = ['dish_name']

        labels = {
            'dish_name': '',
        }

        widgets = {
            'dish_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название блюда'}),
        }


class ReceptForm(ModelForm):
    class Meta:
        model = ReceptModel
        fields = ['ingredient_name', 'count', 'measure']

        widgets = {
            'ingredient_name': TextInput(attrs={'id': 'ingredient_name', 'class': 'form-control', 'placeholder': 'Ингредиент'}),
            'count': NumberInput(attrs={'id': 'count', 'class': 'form-control', 'placeholder': 'Количество'}),
            'measure': Select(attrs={'id': 'measure', 'class': 'form-control', 'placeholder': 'Единица измерения'}),
        }