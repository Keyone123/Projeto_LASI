from django import forms

from aplicativo.models import Produto


class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
