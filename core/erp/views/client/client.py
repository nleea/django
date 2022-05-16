import re
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.erp.forms.clientForm import ClientForm
from core.erp.models import Cliente


class ClientView(TemplateView):
    template_name = 'client/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Cliente.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                form = Cliente()
                form.names = request.POST['names']
                form.date_birthday = request.POST['date_birthday']
                form.gender = request.POST['gender']
                form.direccion = request.POST['direccion']
                form.surnames = request.POST['surnames']
                form.dni = request.POST['dni']
                form.save()
            elif action == 'edit':
                form = Cliente.objects.get(pk=request.POST['id'])
                form.names = request.POST['names']
                form.date_birthday = request.POST['date_birthday']
                form.gender = request.POST['gender']
                form.direccion = request.POST['direccion']
                form.surnames = request.POST['surnames']
                form.dni = request.POST['dni']
                form.save()
            elif action == 'delete':
                form = Cliente.objects.get(pk=request.POST['id'])
                form.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('erp:client')
        context['entity'] = 'Clientes'
        context['action'] = 'add'
        context['form'] = ClientForm()
        return context
