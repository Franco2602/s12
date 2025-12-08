from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Registro
from .forms import RegistroForm

class RegistroListView(LoginRequiredMixin, ListView):
    model = Registro
    template_name = 'core/registro_list.html'
    context_object_name = 'registros'

    def get_queryset(self):
        return Registro.objects.filter(usuario=self.request.user)

class RegistroCreateView(LoginRequiredMixin, CreateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'core/registro_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'core/registro_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Registro.objects.filter(usuario=self.request.user)

class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = Registro
    template_name = 'core/registro_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Registro.objects.filter(usuario=self.request.user)
