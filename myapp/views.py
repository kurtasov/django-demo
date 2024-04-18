from django.http import HttpResponse
from django.template import loader


def hello(request):
    template = loader.get_template('hello_world.html')
    context = {
        'data': ['test1', 'test2', 'test3'],
        'footer_text': 'До свидания!'
    }
    return HttpResponse(template.render(context, request))


def hello_name(request, slug):
    template = loader.get_template('hello_world.html')
    context = {
        'data': ['test1', 'test2', 'test3'],
        'footer_text': f'Привет, {slug}!'
    }
    return HttpResponse(template.render(context, request))
