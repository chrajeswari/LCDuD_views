from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.http import HttpResponse
class school_list(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #queryset=School.objects.filter(id=1)
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'