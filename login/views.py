from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


def home(request):
    return HttpResponse('Honey, I\'m home!')

def login(request):
    context = {}
    template = loader.get_template('test_template.html')
    return HttpResponse(template.render(context, request))

class IndexView(TemplateView):
    template_name = 'test_template.html'