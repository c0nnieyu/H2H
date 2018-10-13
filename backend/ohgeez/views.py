from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Category

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        categories = Category.objects.order_by('name')
        context = { 'categories': categories }
        return render(request, 'index.html', context)

class TestPageView(TemplateView):
  def get(self, request, **kwargs):
    return render(request, 'hello.html', context=None)
