from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from aqua.models import Aqua
from user_app.models import Blue


class Add(CreateView):
    model = Blue
    fields = ('title', 'content', 'app_name')
    template_name = 'add.html'
    success_url = '/blue/'
