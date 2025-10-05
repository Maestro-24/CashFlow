from django.contrib import admin
from .models import *

admin.site.register(Status)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(FinancialRecord)
admin.site.register(OperationType)
