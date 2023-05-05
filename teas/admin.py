from django.contrib import admin
from .models import Tea
from .models import Customer

admin.site.register(Tea)
admin.site.register(Customer)