from django.forms import *
from core.erp.models import Categoria


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        # para agregar con un form si se va a utilizar la misma clase en diferentes elementos del form
        # form.field.widget.attrs['class'] = 'form-control'
        # form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Categoria
        fields = '__all__'
        # labels = {
        #     'nombre': 'Nombre'
        # }
        widgets = {
            'nombre': TextInput(attrs={
                # 'class': 'form-control', # para colocar la clase que se necesite en el elemento form
                'placeholder': 'Categoria',
                # 'autocomplete': 'off'
            }),
            'desc': Textarea(attrs={
                # 'class': 'form-control', # para colocar la clase que se necesite en el elemento form
                'placeholder': 'Descripcion',
                # 'autocomplete': 'off',
                'cols': 3,
                'rows': 3
            })
        }
        # excluir campos para que no aparezcan en el renderizado
        exclude = ['user_create', 'user_update']

    def save(self, commit=True):  # Nos sirve para crear validaciones para el formulario
        form = super()
        data = {}
        try:
            if form.is_valid():
                form.save(commit)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean(self):
        cleaned = super().clean()
        if len(cleaned['nombre']) > 50:
            self.add_error('nombre', "El nombre es demasiado largo")
        return cleaned
