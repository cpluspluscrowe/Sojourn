from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['corresponding_user']
    class Meta:
        model = Person

admin.site.register(Person,PersonAdmin)

