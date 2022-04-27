from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ...models import Categoria
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ...forms.createForm import CategoryForm
from django.urls import reverse_lazy
# from django.shortcuts import render


@method_decorator(login_required, name='dispatch')
class CategoryListView(ListView):
    model = Categoria
    template_name = "category/list.html"
    title = 'Listas categoria'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for element in Categoria.objects.all():
                    data.append(element.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['entity'] = 'Categorias'
        context['form'] = reverse_lazy('erp:category_form')
        context['list_url'] = reverse_lazy('erp:category_form')
        return context


@method_decorator(login_required, name='dispatch')
class CreateCategoryView(CreateView):
    model = Categoria
    template_name = "category/form.html"
    form_class = CategoryForm
    title = 'Crear una categoria'
    success_url = reverse_lazy('erp:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()  # cree un metodo dentro de la clase CategoryForm
            else:
                data['error'] = 'Elegir una opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        # form = CategoryForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect(self.success_url)
        # else:
        #     self.object = None
        #     context = self.get_context_data(**kwargs)
        #     context['form'] = form
        #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['entity'] = 'Listas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['class_icon'] = 'bi bi-plus-lg'
        context['class_icon_save'] = 'bi bi-box-arrow-down'
        context['class_color'] = 'btn btn-primary'
        return context


@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Categoria
    template_name = "category/form.html"
    success_url = reverse_lazy('erp:category_list')
    form_class = CategoryForm
    title = 'Actualizar una categoria'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                # cree un metodo dentro de la clase CategoryForm
                data = form.save()
            else:
                data['error'] = 'Elegir una opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['entity'] = 'Listas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['class_icon'] = 'bi bi-pencil'
        context['class_icon_save'] = 'bi bi-box-arrow-down'
        context['class_color'] = 'btn btn-primary'
        return context


@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('erp:category_list')
    form_class = CategoryForm
    title = 'Delete category'
    template_name = 'category/delete.html'
    template_name_suffix = '_check_delete'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['action'] = 'delete'
        context['class_icon_save'] = 'bi bi-trash-fill'
        context['class_color'] = 'btn btn-danger'
        context['entity'] = 'Listas'
        context['list_url'] = self.success_url
        return context


@method_decorator(login_required, name='dispatch')
class CatergoryFormView(FormView):
    form_class = CategoryForm
    template_name = 'category/form.html'
    success_url = reverse_lazy('erp:category_list')

    def form_invalid(self, form):
        # para poder ver los errores
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        data = {}
        if request.POST['action'] == 'add':
            try:
                form = self.get_form()
                if self.form_valid(form):
                    form.save()
                else:
                    data['error'] = form.errors
            except Exception as e:
                data['error'] = str(e)
        else:
            data['error'] = 'Elegir una opcion'
        return JsonResponse(data, safe=False)

    def form_valid(self, form):
        if form.is_valid():
            return True
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | categoria'
        context['entity'] = 'categoria'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['class_icon'] = 'bi bi-plus-lg'
        context['class_icon_save'] = 'bi bi-box-arrow-down'
        context['class_color'] = 'btn btn-primary'
        return context
