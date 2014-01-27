from django.contrib import admin
from inmueble.models import *
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

class FotoInmuebleInline(admin.TabularInline):
  model=FotoInmueble
  extra=1
  max_num=12

class InmuebleAdmin(admin.ModelAdmin):
  readonly_fields=['id','thumbnails']
  fieldsets=[
    (ugettext_lazy(u'Información Principal'),
      {'fields':['thumbnails','id', 'barrio', 'direccion', 'descripcion', 'tipo_inmueble', 'superficie']}),
    (ugettext_lazy(u'Publicacion'), {'fields':[('precio_dia', 'precio_semana', 'precio_mes'), 'publicado', 'destacado']}),
    (None, {"classes": ("placeholder direccioninmueble_set-group",), "fields" : ()}),
    (None, {"classes": ("placeholder fotoinmueble_set-group",), "fields" : ()}),
    (ugettext_lazy(u'Comodidades y Servicios'),{
      'classes': ('grp-collapse grp-open',),
      'fields':[ 'comodidades', 'servicios',]
      }),
  ]
  inlines=[ FotoInmuebleInline, ]
  list_display=['thumbnail','id','direccion', 'barrio','tipo_inmueble','publicado','destacado','precio_dia', 'precio_semana', 'precio_mes']
  list_display_links = ('thumbnail', 'id')
  list_filter=['tipo_inmueble', 'publicado', 'destacado']
  search_fields=['direccion','barrio','id']
  date_hierarchy='fecha_ingreso'
  filter_horizontal=['comodidades','servicios']
  list_per_page = 40
  actions_on_bottom = True

# Register your models here.
admin.site.register(TipoInmueble)
admin.site.register(Comodidad)
admin.site.register(Servicio)
admin.site.register(Barrio)
admin.site.register(Inmueble,InmuebleAdmin)
