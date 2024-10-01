from django.contrib import admin
import nested_admin
from .models import Interface_module,Mixture_module, Mastering_module, Interface_evaluation, Mixture_evaluation, Mastering_evaluation, User, Top_panel, Options_panel, Side_panel, Workstation, Pregunta, ElegirRespuesta, RespuestaUsuario, Evaluations
from .forms import ElegirInlineFormset

class Top_panel_admin(admin.ModelAdmin):
    search_fields=('name','content', 'status')
    readonly_fields=('progression',)

class Side_panel_admin(admin.ModelAdmin):
    search_fields=('name','content', 'status')
    readonly_fields=('progression',)

class Options_panel_admin(admin.ModelAdmin):
    search_fields=('name','content', 'status')
    readonly_fields=('progression',)

class Workstation_admin(admin.ModelAdmin):
    search_fields=('name','content', 'status')
    readonly_fields=('progression',)

class ElegirRespuestaInline(admin.TabularInline):
    model=ElegirRespuesta
    can_delete=False
    extra=4
    max_num=ElegirRespuesta.MAXIMO_RESPUESTA
    min_num=ElegirRespuesta.MAXIMO_RESPUESTA
    formset=ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    extra = 1
    inlines = [ElegirRespuestaInline, ]
    list_display=['texto', ]
    search_fields=['texto', 'preguntas__texto']

class RespuestaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['fecha_respuesta', 'pregunta', 'respuesta', 'correcta', 'resultado']

    class Meta:
        model=RespuestaUsuario

class Interface_evaluation_admin(admin.ModelAdmin):
    #list_display=('name', 'qualification', 'number_attempts', 'quantity_microModules')
    search_fields=('id','number_attempts','qualification')

class Interface_module_admin(admin.ModelAdmin):
    list_display=('name', 'status', 'progression', 'quantity_microModules')
    search_fields=('id','name','status')

class User_admin(admin.ModelAdmin):
    readonly_fields=('progression',)
    search_fields=('id','name','username','country')



admin.site.register(User, User_admin)
admin.site.register(Interface_module, Interface_module_admin)
admin.site.register(Top_panel, Top_panel_admin)
admin.site.register(Side_panel, Side_panel_admin)
admin.site.register(Options_panel, Options_panel_admin)
admin.site.register(Workstation, Workstation_admin)
admin.site.register(Mixture_module)
admin.site.register(Mastering_module)
admin.site.register(Interface_evaluation, Interface_evaluation_admin)
admin.site.register(Mixture_evaluation)
admin.site.register(Mastering_evaluation)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(RespuestaUsuario)

# Register your models here.
