from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Despesa
from .forms import despesaForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def listaDesp(request):
    lista = Despesa.objects.all().order_by('nome')
    paginator = Paginator(lista, 10)
    page = request.GET.get('page')
    despesas = paginator.get_page(page)
    return render(request, 'listadesp.html', {'despesas': despesas})

@login_required
def addDesp(request):
    if request.method == 'POST':
        form = despesaForm(request.POST)
        if form.is_valid():
            Despesa = form.save()
            return HttpResponseRedirect('/despesas/')
    else:
        form = despesaForm()
        return render(request, 'addDesp.html', {'form':form})

@login_required
def editDesp(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    form = despesaForm(instance=despesa)

    if(request.method == 'POST'):
        form = despesaForm(request.POST, instance=despesa)

        if(form.is_valid()):
            despesa.save()
            return redirect('/despesas')
        else:
            return render(request, 'editardesp.html', {'form':form, 'despesa':despesa})

    else:
        return render(request, 'editardesp.html', {'form':form, 'despesa':despesa})

@login_required
def deletDesp(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    despesa.delete()
    return redirect('/despesas')

@login_required
def despView(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    return render(request, 'despesa.html', {'despesa':despesa})




