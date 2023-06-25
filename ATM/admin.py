from django.contrib import admin

# Register your models here.
from .models import Person,machine
admin.site.register(Person)
admin.site.register(machine)
