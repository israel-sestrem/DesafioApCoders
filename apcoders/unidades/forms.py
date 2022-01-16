from django.forms import ModelForm
from .models import Unidade

class FormUnidade(ModelForm):
    class Meta:
        model = Unidade
        fields = '__all__'