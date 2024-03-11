from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Gasto
from .forms import gastoForm
from django.contrib.auth.decorators import login_required
from usuarios.models import CustomUser
from django.core.paginator import Paginator
import csv

@login_required
def listaGasto(request):
    lista = Gasto.objects.filter(usuario=request.user).order_by('-data')
    paginator = Paginator(lista, 10)
    page = request.GET.get('page')
    gastos = paginator.get_page(page)
    return render(request, 'lista.html', {'gastos': gastos})

@login_required
def addgasto(request):
    if request.method == 'POST':
        form = gastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            return HttpResponseRedirect('/core/')
    else:
        form = gastoForm()
    return render(request, 'addgasto.html', {'form': form})

@login_required    
def editar(request, id):
    gasto = get_object_or_404(Gasto, pk=id)
    form = gastoForm(instance=gasto)

    if(request.method == 'POST'):
        form = gastoForm(request.POST, instance=gasto)

        if(form.is_valid()):
            gasto.save()
            return redirect('/core')
        else:
            return render(request, 'editar.html', {'form':form, 'gasto':gasto})

    else:
        return render(request, 'editar.html', {'form':form, 'gasto':gasto})

@login_required    
def deletar(request, id):
    gasto = get_object_or_404(Gasto, pk=id)
    gasto.delete()
    return redirect('/core')

@login_required
def gastoView(request, id):
    gasto = get_object_or_404(Gasto, pk=id)
    return render(request, 'gasto.html', {'gasto':gasto})
     
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gastos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Valor', 'Tipo', 'Data'])

    gastos = Gasto.objects.all()

    for gasto in gastos:
        writer.writerow([gasto.nome, gasto.valor, gasto.tipo, gasto.data])

    return response


