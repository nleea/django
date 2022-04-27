from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from ..forms import AuthForms


class LoginFormView(LoginView):  # con la Vista LoginView
    template_name = 'login.html'
    next_page = reverse_lazy('erp:dashboard')

    def dispatch(self, request, *args, **kwargs):
        # print(list(request.session.keys()))
        # print(list(request.session.items()))
        # print(request.session.get(lambda x: list(request.session.keys())[x]))
        if request.user.is_authenticated:
            return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context


class LoginFormView2(FormView):  # con la vista FormView
    form_class = AuthenticationForm
    template_name = 'login.html'
    # redireciona a la pagina que le mandamos despues que el user este logueado
    # next_page = reverse_lazy('erp:category_list')
    success_url = reverse_lazy('erp:dashboard')

    def form_valid(self, form):
        user = authenticate(
            username=form.data['username'], password=form.data['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        return HttpResponseRedirect(reverse_lazy('auth:login'))

    def dispatch(self, request, *args, **kwargs):
        # print(list(request.session.keys()))
        # print(list(request.session.items()))
        # print(request.session.get(lambda x: list(request.session.keys())[x]))
        # if request.user.is_authenticated:
        #     return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context


class LogoutFormView(LogoutView):  # Logout con la Vista LoginLogout
    next_page = reverse_lazy('auth:login')


class LogoutFormView2(RedirectView):  # Logout con la Vista RedirectView
    title = 'Logout'
    pattern_name = 'login'

    def patch(self, request, *args, **kwargs):
        logout(request)
        return super().patch(request, *args, **kwargs)


class SignupView(FormView):
    model = User
    form_class = AuthForms
    template_name = 'signup.html'
    success_url = reverse_lazy('erp:dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Signup'
        return context
