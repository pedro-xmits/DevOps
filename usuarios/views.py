from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from django.contrib.auth import authenticate, login
from .forms import cadastroForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def listaUser(request):
    lista = CustomUser.objects.all().order_by('username')
    paginator = Paginator(lista, 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'listauser.html', {'users':users})

@login_required
def cadastro(request):
    if request.method == 'POST':
        form = cadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/usuarios')
    else:
        form = cadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def loginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else: 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            return HttpResponse('autenticado')
        else:
            return HttpResponse('Username ou senha incorretos')
    return HttpResponseRedirect('/core')

@login_required    
def editar(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    form = cadastroForm(instance=user)

    if(request.method == 'POST'):
        form = cadastroForm(request.POST, instance=user)

        if(form.is_valid()):
            user.save()
            return redirect('/usuarios')
        else:
            return render(request, 'editar.html', {'form':form, 'user':user})

    else:
        return render(request, 'editar.html', {'form':form, 'user':user})

@login_required    
def deletar(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    user.delete()
    return redirect('/usuarios')

