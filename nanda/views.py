from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Diagnoses

class DiagnosesListView(ListView):
    model: Diagnoses
    template_name: "nanda/diagnoses.html"
    queryset = Diagnoses.objects.all()
    context_object_name: 'diagnoses_list'

class DiagnosesDetailView(DetailView):
    model = Diagnoses