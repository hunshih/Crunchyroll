from django.contrib import admin
from api.models import Dummy
from api.models import Todo

# Register your models here.
admin.site.register(Dummy)
admin.site.register(Todo)