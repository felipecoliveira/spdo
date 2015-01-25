from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.edit import (CreateView, FormView
                                      ,UpdateView, DeleteView)

from core.models import Area

class AreaView(ListView):
   model = Area
   context_object_name = 'areas'
   template_name = 'core/area/list.html'

