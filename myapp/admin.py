from django.contrib import admin

# Register your models here.
from myapp.models import Categories, Customers
admin.site.register(Categories)
admin.site.register(Customers)
