from django.forms import ModelForm
from .models import Despesa

class FormDespesa(ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'