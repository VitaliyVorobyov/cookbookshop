from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from .models import DishModel, ReceptModel
from .forms import DishForm, ReceptForm


# Create your views here.
def index(request):
    return render(request, 'recept/index.html')


def recepts(request):
    data = ReceptModel.objects.all()
    return render(request, 'recept/recepts.html', {'data': data})


def newdish(request):
    return render(request, 'recept/new-dish.html')


class ReceptView(DeleteView):
    model = ReceptModel
    template_name = 'recept/view-recept.html'
    success_url = '/'


class DishView(DeleteView):
    model = DishModel
    template_name = 'recept/new-dish.html'
    success_url = '/'


def new_dish(request):
    errors = ''
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_ingredient', form.instance.pk)
        else:
            errors = 'Форма заполнена неверно'

    form = DishForm()

    data = {
        'form': form,
        'errors': errors
    }

    return render(request, 'recept/new-dish.html', data)


def new_ingredient(request, pk):
    errors = ''
    if request.method == 'POST':
        form = ReceptForm(request.POST)
        if form.is_valid():
            form.instance.dish = DishModel.objects.get(pk=int(pk))
            form.save()
            return redirect('new_ingredient', pk)
        else:
            errors = 'Форма заполнена неверно'

    form = ReceptForm()

    data = {
        'form': form,
        'errors': errors
    }

    return render(request, 'recept/new-ingredient.html', data)
