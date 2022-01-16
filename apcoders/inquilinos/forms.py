from django.forms import ModelForm
from .models import Inquilino

class FormInquilino(ModelForm):
    class Meta:
        model = Inquilino
        fields = '__all__'