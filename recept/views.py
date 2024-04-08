from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import DishModel, ReceptModel
from .forms import DishForm, ReceptForm


# Create your views here.
def index(request):
    return render(request, 'recept/index.html')


def recepts(request):
    page_number = int(request.GET.get('page', 1))
    data = DishModel.objects.all()
    paginator = Paginator(data, 2)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'recept/recepts.html', context)


def newdish(request):
    return render(request, 'recept/new-dish.html')


class DishView(DetailView):
    model = DishModel
    template_name = 'recept/view-recept.html'
    context_object_name = 'dish'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = self.get_object()
        ingredints = ReceptModel.objects.filter(dish=dish)

        context['dish'] = dish
        context['ingredints'] = ingredints

        return context


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
