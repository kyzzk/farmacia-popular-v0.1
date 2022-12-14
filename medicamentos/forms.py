from django.forms import ModelForm
from .models import Medicamento


class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['name', 'mg', 'indication', 'code']
