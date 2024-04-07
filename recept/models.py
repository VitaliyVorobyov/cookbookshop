from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class DishModel(models.Model):
    dish_name = models.CharField('Название блюда', max_length=100, unique=True)

    def __str__(self):
        return self.dish_name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class ReceptModel(models.Model):
    MEASURES = [
        ('шт', 'шт'),
        ('кг', 'кг'),
        ('г', 'г'),
        ('л', 'л'),
        ('мл', 'мл'),
    ]
    dish = models.ForeignKey(DishModel, on_delete=models.CASCADE, related_name='dish', verbose_name='Блюдо')
    ingredient_name = models.CharField('Ингредиент', max_length=100)
    count = models.IntegerField('Количество', default=1, validators=[MinValueValidator(1)])
    measure = models.CharField('Единица измерения', max_length=2, choices=MEASURES, default='шт')

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
