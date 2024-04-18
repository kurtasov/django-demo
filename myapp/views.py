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


def hello_with_params(request):
    template = loader.get_template('hello_world.html')
    context = {
        'param1': request.GET['param1'], 'param2': request.GET['param2'],
        'data': ['test1', 'test2', 'test3'],
        'footer_text': 'До свидания!'
    }
    return HttpResponse(template.render(context, request))


def show_form(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render(None, request))


def show_form_data(request):
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"Имя: {name}<br>Возраст: {age}")