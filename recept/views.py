from django.shortcuts import render
from django.views.generic import DetailView, View, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .models import DishModel, ReceptModel
from .forms import DishForm, ReceptForm


class IndexView(View):
    template_name = 'recept/index.html'

    def get(self, request):
        return render(request, self.template_name)


class ReceptsView(ListView):
    model = DishModel
    template_name = 'recept/recepts.html'
    context_object_name = 'page'
    paginate_by = 4
    ordering = ['dish_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DishView(FormMixin, DetailView):
    model = DishModel
    form_class = ReceptForm
    template_name = 'recept/view-recept.html'
    context_object_name = 'dish'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = self.get_object()
        ingredients = ReceptModel.objects.filter(dish=dish).order_by('ingredient_name')
        per = self.request.GET.get('per', '')

        if per:
            try:
                per = int(per)
                for ingredient in ingredients:
                    ingredient.count *= per
            except ValueError:
                pass

        context['dish'] = dish
        context['ingredients'] = ingredients
        context['per'] = per
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.dish = DishModel.objects.get(pk=int(pk))
        form.save()
        return super().form_valid(form)


class NewDishView(CreateView):
    model = DishModel
    form_class = DishForm
    template_name = 'recept/new-dish.html'

    def get_success_url(self):
        pk = self.object.pk
        return f'/recepts/{pk}'


class DeleteDishView(DeleteView):
    model = DishModel
    template_name = 'recept/delete-dish.html'
    success_url = '/recepts/'


class DeleteIngredientView(DeleteView):
    model = ReceptModel
    template_name = 'recept/delete-dish.html'

    def get_success_url(self):
        pk = self.object.dish.pk
        return f'/recepts/{pk}'


class UpdateDishView(UpdateView):
    model = ReceptModel
    form_class = ReceptForm
    template_name = 'recept/edit-ingredient.html'

    def get_success_url(self):
        pk = self.object.dish.pk
        return f'/recepts/{pk}'
