from django.forms import ModelForm, Select
from ..models import Producto


class FormProduct(ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'id_cat': Select(attrs={
                'name': 'id_cat',
                'id': 'id_cat',
                'class': 'select'
            })
        }

    def save(self):  # Nos sirve para crear validaciones para el formulario
        form = super()
        data = {}
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
