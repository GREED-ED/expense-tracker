from django.contrib import admin
from .models import Expense, User


admin.site.register(User)
admin.site.register(Expense)