# coding=utf-8
from django.db import models
from iampacks.cross.direccion.models import Direccion
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from datetime import date
from iampacks.cross.gmap.models import Geocoder
from django.core.exceptions import ValidationError

class TipoInmueble(models.Model):
  descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripcion'))
  class Meta:
    ordering = ['descripcion']
    verbose_name = ugettext_lazy(u"Tipo de Inmueble")
    verbose_name_plural = ugettext_lazy(u"Tipos de Inmueble")
  def __unicode__(self):
    return u'%s' % self.descripcion

class Comodidad(models.Model):
  descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripcion'))
  class Meta:
    ordering = ['descripcion']
    verbose_name = ugettext_lazy(u"Comodidad")
    verbose_name_plural = ugettext_lazy(u"Comodidades")
  def __unicode__(self):
    return u'%s' % self.descripcion

class Servicio(models.Model):
  descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripcion'))
  class Meta:
    ordering = ['descripcion']
    verbose_name = ugettext_lazy(u"Servicio")
    verbose_name_plural = ugettext_lazy(u"Servicios")
  def __unicode__(self):
    return u'%s' % self.descripcion

class Barrio(models.Model):
  descripcion = models.CharField(max_length=60, unique=True, verbose_name=ugettext_lazy(u'Descripcion'))
  class Meta:
    ordering = ['descripcion']
    verbose_name = ugettext_lazy(u"Barrio")
    verbose_name_plural = ugettext_lazy(u"Barrios")
  def __unicode__(self):
    return u'%s' % self.descripcion

class Inmueble(models.Model):
  barrio = models.ForeignKey(Barrio,verbose_name=ugettext_lazy(u'Barrio'), null=True, editable=False)
  direccion = models.CharField(max_length=200, verbose_name=ugettext_lazy(u'Direccion'))
  direccion_gmap = models.CharField(max_length=200, verbose_name=ugettext_lazy(u'Direccion gmap'), null=True, editable=False)
  descripcion = models.TextField(verbose_name=ugettext_lazy(u'Descripcion'), null=True, blank=True)
  tipo_inmueble = models.ForeignKey(TipoInmueble,verbose_name=ugettext_lazy(u'Tipo de Inmueble'), null=True, blank=True)
  superficie = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  precio_dia = models.DecimalField(ugettext_lazy(u'Dia (u$s)'), max_digits=8, decimal_places=2, null=True, blank=True)
  precio_semana= models.DecimalField(ugettext_lazy(u'Semana (u$s)'), max_digits=8, decimal_places=2, null=True, blank=True)
  precio_mes= models.DecimalField(ugettext_lazy(u'Mes (u$s)'), max_digits=8, decimal_places=2, null=True, blank=True)
  publicado = models.BooleanField(blank=True,verbose_name=ugettext_lazy(u'Publicado'))
  destacado = models.BooleanField(blank=True,verbose_name=ugettext_lazy(u'Destacado'))
  fecha_ingreso = models.DateField(default=date.today(), verbose_name=ugettext_lazy(u'Fecha Ingreso'))
  comodidades = models.ManyToManyField(Comodidad, blank=True, verbose_name=ugettext_lazy(u'Comodidades'))
  servicios = models.ManyToManyField(Servicio, blank=True, verbose_name=ugettext_lazy(u'Servicios'))
  latitud = models.DecimalField(ugettext_lazy(u'Latitud'), max_digits=13, decimal_places=7, null=True, blank=True, editable=False)
  longitud = models.DecimalField(ugettext_lazy(u'Longitud'), max_digits=13, decimal_places=7, null=True, blank=True, editable=False)
  def __unicode__(self):
    if self.barrio:
      return u'%s - %s' % (self.barrio, self.direccion) 
    return u'%s' % self.id

  class Meta:
    verbose_name = ugettext_lazy(u"Inmueble")
    verbose_name_plural = ugettext_lazy(u"Inmuebles")

  def thumbnail(self):
    url = ''
    if any(self.fotoinmueble_set.order_by('id')):
      url = self.fotoinmueble_set.order_by('id')[:1][0].thumbnail.url
    return "<img src='%s' height=100 />" % url
  thumbnail.allow_tags = True
  thumbnail.short_description = ugettext_lazy(u'Foto')

  def thumbnails(self,cantidad=0):
    html=''
    fotos=self.fotoinmueble_set.order_by('id')
    i=0
    for foto in fotos:
      if cantidad>0 and i>=cantidad:
        break
      url = foto.foto.url
      url_thumbnail = foto.thumbnail.url
      html = html + "<a href='%s' target='blank'><img src='%s' height=100 /></a>" % (url,url_thumbnail)
      i+=1
    return html
  thumbnails.allow_tags = True
  thumbnails.short_description = ugettext_lazy(u'Fotos')

  def admin_url(self):
    return '/admin/inmueble/inmueble/%s/'%self.id

  def clean(self, *args, **kwargs):
    self.direccion_gmap = None
    self.barrio = None
    self.latitud = None
    self.longitud = None
    try:
      gmap = Geocoder(self.direccion)
      self.direccion_gmap = gmap.direccion_completa()
      self.barrio = Barrio.objects.get_or_create(descripcion=gmap.barrio())[0]
      self.barrio.save()
      self.latitud = gmap.latitud()
      self.longitud = gmap.longitud()
    except Exception:
      raise ValidationError(_(u'No se ha podido determinar la direccion en el mapa.'))
    super(Inmueble,self).clean(*args, **kwargs)

  def precios(self):
    listado_precios = []
    if self.precio_dia and self.precio_dia != 0:
      listado_precios.append('%s u$s' % self.precio_dia)
    if self.precio_semana and self.precio_semana != 0:
      listado_precios.append('%s u$s' % self.precio_semana)
    if self.precio_mes and self.precio_mes != 0:
      listado_precios.append('%s u$s' % self.precio_mes)
    return ' - '.join(listado_precios)

  def infowindow(self):
    return '<h2>#%(id)s - %(direccion)s</h2>  <h3>%(barrio)s</h3> <h4>%(precios)s</h4> <p>%(thumbnails)s</p>' % {
      'id': self.id,
      'direccion': self.direccion,
      'barrio': self.barrio,
      'precios': self.precios(),
      'thumbnails': self.thumbnails(3),
    }

class ImageField(models.ImageField):

  def __init__(self, *args, **kwargs):
    super(ImageField, self).__init__(*args, **kwargs)

  def clean(self, *args, **kwargs):
    data = super(ImageField, self).clean(*args, **kwargs)
    data.name = data.name.encode('ascii','ignore')
    return data

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^inmueble\.models\.ImageField"])

class FotoInmueble(models.Model):
  inmueble = models.ForeignKey(Inmueble)
  foto = ImageField(upload_to=u'inmueble/foto/', blank=True )
  thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(100,100)], image_field='foto', format='JPEG', options={'quality': 90})
  mini_thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(60,60)], image_field='foto', format='JPEG', options={'quality': 90})
  def __unicode__(self):
    return self.foto.url
  class Meta:
    verbose_name = ugettext_lazy(u"Foto Inmueble")
    verbose_name_plural = ugettext_lazy(u"Fotos Inmueble")

"""
class Alquiler(models.Model):
  inmueble = models.ForeignKey(Inmueble, verbose_name=ugettext_lazy(u'Inmueble'))
  fecha_desde = models.DateField(verbose_name=ugettext_lazy(u'Fecha Desde'))
  fecha_hasta= models.DateField(verbose_name=ugettext_lazy(u'Fecha Hasta'))
  precio = models.DecimalField(ugettext_lazy(u'Precio (u$s)'), max_digits=8, decimal_places=2, null=True, blank=True)
"""
