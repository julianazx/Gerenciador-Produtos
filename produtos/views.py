from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ProdutoForm
from .models import Produtos

# Create your views here.
def index(request):
    return render(request, 'produtos/index.html', {
        'produtos': Produtos.objects.all()
    })

def view_produto(request, id):
    produto = Produtos.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':        
        form = ProdutoForm(request.POST)
        if form.is_valid():
            new_produto = Produtos(
                numero_produto=form.cleaned_data['numero_produto'],
                nome_produto=form.cleaned_data['nome_produto'],
                marca=form.cleaned_data['marca'],
                email=form.cleaned_data['email'],
                category=form.cleaned_data['category'],
                quantidade=form.cleaned_data['quantidade'],
            )
            new_produto.save()
            return render(request, 'produtos/add.html', {
                'form': ProdutoForm(),
                'success': True
            })
        else:
            form = ProdutoForm()
            return render(request, 'produtos/add.html', {
            'form': form
        })

    # If the request method is GET, return the add form

    return render(request, 'produtos/add.html', {
        'form': ProdutoForm()
    })

def edit(request, id):
    if request.method == 'POST':
        produto = Produtos.objects.get(pk=id)
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return render(request, 'produtos/edit.html', {
            'form': form,
            'success': True
        })
    else:
        produto = Produtos.objects.get(pk=id)
        form = ProdutoForm(instance=produto)
        return render(request, 'produtos/edit.html', {
        'form': form
    })    

def delete(request, id):
  if request.method == 'POST':
    produto = Produtos.objects.get(pk=id)
    produto.delete()
  return HttpResponseRedirect(reverse('index')) 