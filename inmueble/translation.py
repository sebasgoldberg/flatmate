from modeltranslation.translator import translator, TranslationOptions
from inmueble.models import *

class TipoInmuebleTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(TipoInmueble, TipoInmuebleTranslationOptions)

class ComodidadTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Comodidad, ComodidadTranslationOptions)

class ServicioTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Servicio, ServicioTranslationOptions)

class InmuebleTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(Inmueble, InmuebleTranslationOptions)

