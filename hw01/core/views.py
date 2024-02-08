from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Article
from hw01.settings import GROUPS


def main_page(request):
    template = 'main.html'
    context = {'groups': GROUPS}
    return render(request, template, context)


def group_page(request, group):
    template = 'group.html'
    articles = get_object_or_404(Article, group=group)
    context = {'articles': articles}
    return render(request, template, context)


def contact(request):
    return redirect('core:main')


def task(request):
    return redirect('core:main')


def author(request):
    return redirect('core:main')


def tech(request):
    return redirect('core:main')
