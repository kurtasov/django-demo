from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from wildewidgets import DataTable
from myapp.models import Customers


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


class TableView(TemplateView):  # See https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
    template_name = ("datatable.html")

    def get_context_data(self, **kwargs):
        table = DataTable()
        table.add_column('name')
        table.add_column('rating')
        table.add_column('age')
        table.add_row(name='Кулишенко', rating=53, age=25)
        table.add_row(name='Некрасов', rating=63, age=24)
        table.add_row(name='Пономаренко', rating=73, age=23)
        table.add_row(name='Шумейко', rating=53, age=25)
        table.add_row(name='Колобова', rating=63, age=24)
        table.add_row(name='Рыбакова', rating=73, age=23)
        table.add_row(name='Чикольба', rating=53, age=25)
        table.add_row(name='Тимошенко', rating=63, age=24)
        table.add_row(name='Зиновьева', rating=73, age=23)
        table.add_row(name='Козлова', rating=53, age=25)
        table.add_row(name='Пономаренко', rating=63, age=24)
        table.add_row(name='Мельников', rating=73, age=23)
        table.add_row(name='Овчаренко', rating=53, age=25)
        table.add_row(name='Терентьева', rating=63, age=24)
        table.add_row(name='Чикольба', rating=73, age=23)
        table.add_row(name='Коломоец', rating=53, age=25)
        table.add_row(name='Рожков', rating=63, age=24)
        table.add_row(name='Шаров', rating=73, age=23)
        table.add_row(name='Зайцева', rating=53, age=25)
        table.add_row(name='Ильина', rating=63, age=24)
        table.add_row(name='Иванов', rating=73, age=23)
        table.add_row(name='Виноградова', rating=53, age=25)
        table.add_row(name='Горобчук', rating=63, age=24)
        table.add_row(name='Борисова', rating=73, age=23)
        table.add_row(name='Ерёменко', rating=73, age=23)
        table.add_row(name='Медведев', rating=53, age=25)
        table.add_row(name='Соболев', rating=63, age=24)
        table.add_row(name='Чикольба', rating=73, age=23)
        table.add_row(name='Фокина', rating=73, age=23)
        table.add_row(name='Фомичёва', rating=53, age=25)
        table.add_row(name='Фролова', rating=63, age=24)
        table.add_row(name='Игнатьев', rating=73, age=23)
        table.add_row(name='Дементьев', rating=63, age=24)
        table.add_row(name='Дзюба', rating=73, age=23)
        kwargs['table'] = table
        return super().get_context_data(**kwargs)


class DbTableView(TemplateView):
    template_name = ("dbtable.html")

    def get_context_data(self, **kwargs):
        table = DataTable()
        data = Customers.objects.all()

        table.add_column('CompanyName')
        table.add_column('Address')
        table.add_column('City')
        table.add_column('Region')
        table.add_column('PostalCode')

        for o in data:
            table.add_row(CompanyName=o.companyname, Address=o.address, City=o.city, Region=o.region, PostalCode=o.postalcode)

        kwargs['dbtable'] = table
        return super().get_context_data(**kwargs)