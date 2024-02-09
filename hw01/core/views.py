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
    articles = Article.objects.filter(group=group)
    context = {'articles': articles}
    return render(request, template, context)


def article_page(request, slug):
    template = 'article.html'
    article = get_object_or_404(Article, slug=slug)
    context = {'article': article}
    return render(request, template, context)

def contact(request):
    return redirect('core:main')


def task(request):
    return redirect('core:main')


def about(request):
    template = 'about.html'
    context = {
        'my': {
            'name': 'Горбенко Игорь Денисович',
            'phone': '+79168946969',
            'mail': 'idgorbenko@edu.hse.ru',
            'educ': 'умный, красивый, талантливый',
            'imgurl': 'https://upload.wikimedia.org/wikipedia/commons/6/66/Siamese_cat_2.jpg'
        },
        'program': {
            'name': 'Экономика',
            'description': 'Экономика должна быть экономной',
            'ruk': {
                'name': 'Кирилл Александрович Букин',
                'mail': 'kabukin@hse.ru',
                'imgurl' :'https://www.hse.ru/pubs/share/thumb/187225977:c2103x2103+50+0:r380x380!.jpg'
            },
            'man': {
                'name': 'Макарова Галина Викторовна',
                'mail': 'gvmakarova@hse.ru',
                'imgurl' :'https://www.hse.ru/pubs/share/thumb/223562260:c527x527+93+0:r380x380!.jpg'
            }
        },
        'pal1': {
            'name': 'Куцев Владимир',
            'phone': '+79858940010',
            'mail': 'vmkutsev@edu.hse.ru',
            'imgurl': 'https://upload.wikimedia.org/wikipedia/commons/6/6c/1Dog-rough-collie-portrait.jpg'
        },
        'pal2': {
            'name': 'Ермаков Тимур',
            'phone': '+79167777070',
            'mail': 'termakov@edu.hse.ru',
            'imgurl': 'https://upload.wikimedia.org/wikipedia/commons/0/0c/Парагвайская_анаконда_в_Гродно.JPG'
        },
    }
    return render(request, template, context)


def tech(request):
    return redirect('core:main')
