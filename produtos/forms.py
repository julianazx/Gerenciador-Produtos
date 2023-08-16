from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['numero_produto', 'nome_produto', 'marca', 'email', 'category', 'quantidade']
        labels = {
            'numero_produto': 'Numero do Produto',
            'nome_produto': 'Nome', 
            'marca': 'Marca', 
            'email': 'Email', 
            'category': 'Category', 
            'quantidade': 'Quantidade'
        }
        widgets = {
            'numero_produto': forms.NumberInput(attrs={'class': 'form-control'}) ,
            'nome_produto': forms.TextInput(attrs={'class': 'form-control'}), 
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'category': forms.TextInput(attrs={'class': 'form-control'}), 
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'})
        }