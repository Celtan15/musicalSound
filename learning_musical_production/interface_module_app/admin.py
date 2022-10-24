from django.contrib import admin

from .models import Interface_evaluation, Interface_module, User


class Interface_module_admin(admin.ModelAdmin):
    list_display=('name', 'status', 'progression', 'quantity_microModules')

admin.site.register(User)
admin.site.register(Interface_module, Interface_module_admin)
admin.site.register(Interface_evaluation)