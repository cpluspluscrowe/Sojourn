from django.contrib import admin
from .models import Check, Cash

class CheckAdmin(admin.ModelAdmin):
    list_display = ['amount']
    class Meta:
        model = Check

admin.site.register(Check,CheckAdmin)



class CashAdmin(admin.ModelAdmin):
    list_display = ['amount']
    class Meta:
        model = Cash

admin.site.register(Cash,CashAdmin)