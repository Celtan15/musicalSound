from django.contrib import admin

from .models import Interface_evaluation, Interface_module, User

class Interface_evaluation_admin(admin.ModelAdmin):
    #list_display=('name', 'qualification', 'number_attempts', 'quantity_microModules')
    search_fields=('id','number_attempts','qualification')

class Interface_module_admin(admin.ModelAdmin):
    list_display=('name', 'status', 'progression', 'quantity_microModules')
    search_fields=('id','name','status')

class User_interface_admin(admin.ModelAdmin):
    readonly_fields=('progression',)
    search_fields=('id','name','nickname','country')

admin.site.register(User, User_interface_admin)
admin.site.register(Interface_module, Interface_module_admin)
admin.site.register(Interface_evaluation, Interface_evaluation_admin)