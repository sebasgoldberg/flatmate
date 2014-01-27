from django.contrib import admin
from inmueble.forms import DireccionInmuebleForm
from inmueble.models import *
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from iampacks.cross.direccion.admin import BaseDireccionInline
from cities_light.models import Country, Region, City

class DireccionInmuebleInline(admin.TabularInline):
  form = DireccionInmuebleForm
  model=DireccionInmueble
  extra = 1
  max_num = 1
  can_delete=False
  fieldsets=[
    (None, {'fields':['barrio', 'direccion']}),
  ]

class FotoInmuebleInline(admin.TabularInline):
  model=FotoInmueble
  extra=1
  max_num=12

class InmuebleAdmin(admin.ModelAdmin):
  readonly_fields=['id','thumbnails']
  fieldsets=[
    (None, {'fields':['thumbnails','id', 'titulo', 'descripcion', 'tipo_inmueble', 'superficie']}),
    (ugettext_lazy(u'Publicacion'), {'fields':[('precio_dia', 'precio_semana', 'precio_mes'), 'publicado', 'destacado']}),
    (None, {"classes": ("placeholder direccioninmueble_set-group",), "fields" : ()}),
    (None, {"classes": ("placeholder fotoinmueble_set-group",), "fields" : ()}),
    (ugettext_lazy(u'Comodidades y Servicios'),{
      'classes': ('grp-collapse grp-open',),
      'fields':[ 'comodidades', 'servicios',]
      }),
  ]
  inlines=[ DireccionInmuebleInline, FotoInmuebleInline, ]
  list_display=['thumbnail','id','titulo','tipo_inmueble','publicado','destacado','precio_dia', 'precio_semana', 'precio_mes']
  list_display_links = ('thumbnail', 'id')
  list_filter=['tipo_inmueble', 'publicado', 'destacado']
  search_fields=['titulo','id']
  date_hierarchy='fecha_ingreso'
  filter_horizontal=['comodidades','servicios']
  list_per_page = 40
  actions_on_bottom = True

# Register your models here.
admin.site.register(TipoInmueble)
admin.site.register(Comodidad)
admin.site.register(Servicio)
admin.site.register(Inmueble,InmuebleAdmin)
admin.site.unregister(Country)
admin.site.unregister(Region)
admin.site.unregister(City)
