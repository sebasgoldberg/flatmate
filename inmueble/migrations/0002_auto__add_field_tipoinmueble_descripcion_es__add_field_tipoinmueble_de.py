# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TipoInmueble.descripcion_es'
        db.add_column(u'inmueble_tipoinmueble', 'descripcion_es',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TipoInmueble.descripcion_en'
        db.add_column(u'inmueble_tipoinmueble', 'descripcion_en',
                      self.gf('django.db.models.fields.CharField')(max_length=60, unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TipoInmueble.descripcion_es'
        db.delete_column(u'inmueble_tipoinmueble', 'descripcion_es')

        # Deleting field 'TipoInmueble.descripcion_en'
        db.delete_column(u'inmueble_tipoinmueble', 'descripcion_en')


    models = {
        u'inmueble.barrio': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Barrio'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.comodidad': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Comodidad'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.fotoinmueble': {
            'Meta': {'object_name': 'FotoInmueble'},
            'foto': ('inmueble.models.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Inmueble']"})
        },
        u'inmueble.inmueble': {
            'Meta': {'object_name': 'Inmueble'},
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Barrio']", 'null': 'True'}),
            'comodidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Comodidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'direccion_gmap': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 31, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '7', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '7', 'blank': 'True'}),
            'precio_dia': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'precio_mes': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'precio_semana': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {}),
            'servicios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Servicio']", 'symmetrical': 'False', 'blank': 'True'}),
            'superficie': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.TipoInmueble']", 'null': 'True', 'blank': 'True'})
        },
        u'inmueble.servicio': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Servicio'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.tipoinmueble': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'TipoInmueble'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'descripcion_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion_es': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inmueble']