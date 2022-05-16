from time import clock_getres
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ...models import Producto
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ...forms.formProduct import FormProduct


@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    template_name = 'product/list.html'
    model = Producto

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product'
        return context


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Producto
    form_class = FormProduct
    template_name = 'product/form.html'
    success_url = reverse_lazy('erp:product_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['action'] == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Elige una opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Producto'
        context['action'] = 'add'
        context['class_icon'] = 'bi bi-plus-lg'
        context['class_icon_save'] = 'bi bi-box-arrow-down'
        context['class_color'] = 'btn btn-primary'
        return context


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Producto
    form_class = FormProduct
    template_name = 'product/form.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.POST['action'] == 'edit':
                form = self.get_form()
                form.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Producto'
        context['action'] = 'edit'
        context['class_icon'] = 'bi bi-plus-lg'
        context['class_icon_save'] = 'bi bi-box-arrow-down'
        context['class_color'] = 'btn btn-primary'
        return context


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    template_name = 'product/delete.html'
    success_url = reverse_lazy('erp:product_list')
    model = Producto
    form_class = FormProduct
    template_name_suffix = '_check_delete'
    title = 'Eliminar Producto'

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
        context['class_icon'] = 'bi bi-plus-lg'
        context['class_icon_save'] = 'bi bi-box-arrow-down'
        context['class_color'] = 'btn btn-primary'
        context['entity'] = 'Listas'
        context['list_url'] = self.success_url
        return context
