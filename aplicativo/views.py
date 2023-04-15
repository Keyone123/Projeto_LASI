from django.urls import reverse_lazy
import django.views.generic
from aplicativo.models import Produto

# Create your views here.

class ProdutoList(django.views.generic.ListView):
    model = Produto
    queryset = Produto.objects.all()


class ProdutoCreate(django.views.generic.CreateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('aplicativo:list')


class ProdutoUpdate(django.views.generic.UpdateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('aplicativo:list')


class ProdutoDetail(django.views.generic.DetailView):
    model = Produto
    queryset = Produto.objects.all()


class ProdutoDelete(django.views.generic.DeleteView):
    queryset = Produto.objects.all()
    success_url = reverse_lazy('aplicativo:list')


class ProdutoMenu(django.views.generic.TemplateView):
    template_name = 'menu.html'
