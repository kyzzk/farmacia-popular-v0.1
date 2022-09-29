from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Medicamento
from .forms import MedicamentoForm


@login_required
def medicamentos_list(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamento.html', {'medicamentos': medicamentos})


@login_required
def medicamentos_new(request):
    form = MedicamentoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('medicamentos_list')
    return render(request, 'medicamento_form.html', {'form': form})


@login_required
def medicamentos_update(request, id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    form = MedicamentoForm(request.POST or None, request.FILES or None, instance=medicamento)

    if form.is_valid():
        form.save()
        return redirect('medicamentos_list')

    return render(request, 'medicamento_form.html', {'form': form})


@login_required
def medicamentos_delete(request, id):
    medicamento = get_object_or_404(Medicamento, pk=id)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamentos_list')

    return render(request, 'person_delete_confirm.html', {'medicamentos': medicamento})