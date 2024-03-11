from django.shortcuts import render, redirect
from .models import CustomUser, Gasto, Correcao
from .forms import CorrecaoForm
from django.core.paginator import Paginator

def criar_correcao(request):
    if request.method == 'POST':
        form = CorrecaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/correcoes')
    else:
        form = CorrecaoForm()

    usuarios = CustomUser.objects.all()

    return render(request, 'addCorre.html', {'form': form, 'usuarios': usuarios})

def listaCorre(request):
    lista = Correcao.objects.all()
    paginator = Paginator(lista, 10)
    page = request.GET.get('page')
    correcoes = paginator.get_page(page)
    return render(request, 'lista.html', {'correcoes': correcoes})
