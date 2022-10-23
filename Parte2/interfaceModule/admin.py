from django.contrib import admin
from interfaceModule.models import InterfaceModule
from interfaceModule.models import InterfaceEvaluation
from interfaceModule.models import Person

class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'nickname', 'email', 'country', 'date_birth')
    search_fields=('id', 'name', 'nickname', 'email')
    list_filter=('name', 'date_birth', 'country')

class ModuleAdmin(admin.ModelAdmin):
    list_display=('name', 'status', 'moduleLocked')
    search_fields=('id', 'name', 'status')
    list_filter=('status', 'progression')

class ModuleEvaluation(admin.ModelAdmin):
    list_display=('name', 'id', 'questions')
    search_fields=('id', 'name', 'qualification')
    list_filter=('qualification', 'name')

admin.site.register(Person, UserAdmin)
admin.site.register(InterfaceModule, ModuleAdmin)
admin.site.register(InterfaceEvaluation, ModuleEvaluation)
# Register your models here.
