from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entrada

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Entrada
    
class EntradaDetailView(DetailView):
    
    template_name = 'entrada_detail.html'
    model = Entrada
    
    
    