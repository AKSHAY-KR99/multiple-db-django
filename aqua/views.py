from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from aqua.models import Aqua


class Add(CreateView):
    model = Aqua
    fields = ('title', 'content', 'app_name')
    template_name = 'add.html'
    success_url = '/aqua/'
