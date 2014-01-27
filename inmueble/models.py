from django.db import models
from iampacks.cross.direccion.models import Direccion
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from datetime import date

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

class Inmueble(models.Model):
  titulo = models.CharField(max_length=200, verbose_name=ugettext_lazy(u'Titulo'))
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
  def __unicode__(self):
    direccion = self.direccioninmueble_set.first()
    if not direccion:
      return u'%s' % self.titulo
    return u'%s' % direccion

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

  def thumbnails(self):
    html=''
    fotos=self.fotoinmueble_set.order_by('id')
    for foto in fotos:
      url = foto.foto.url
      url_thumbnail = foto.thumbnail.url
      html = html + "<a href='%s'><img src='%s' height=100 /></a>" % (url,url_thumbnail)
    return html
  thumbnails.allow_tags = True
  thumbnails.short_description = ugettext_lazy(u'Fotos')

class DireccionInmueble(Direccion):
  inmueble = models.ForeignKey(Inmueble,null=False, blank=False, verbose_name=ugettext_lazy(u'Inmueble'))
  class Meta(Direccion.Meta):
    verbose_name = ugettext_lazy(u"Direccion Inmueble")
    verbose_name_plural = ugettext_lazy(u"Direcciones Inmueble")

class FotoInmueble(models.Model):
  inmueble = models.ForeignKey(Inmueble)
  foto = models.ImageField(upload_to='inmueble/foto/', blank=True )
  thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(100,100)], image_field='foto', format='JPEG', options={'quality': 90})
  mini_thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(60,60)], image_field='foto', format='JPEG', options={'quality': 90})
  def __unicode__(self):
    return self.foto.url
  class Meta:
    verbose_name = ugettext_lazy(u"Foto Inmueble")
    verbose_name_plural = ugettext_lazy(u"Fotos Inmueble")
