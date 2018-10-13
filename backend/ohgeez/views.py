from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

#def index(request):
#  return HttpResponse("Hello, world")

class HomePageView(TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'index.html', context=None)

class TestPageView(TemplateView):
  template_name = "test.html"
