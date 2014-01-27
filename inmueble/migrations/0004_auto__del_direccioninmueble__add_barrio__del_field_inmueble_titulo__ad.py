# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DireccionInmueble'
        db.delete_table(u'inmueble_direccioninmueble')

        # Adding model 'Barrio'
        db.create_table(u'inmueble_barrio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'inmueble', ['Barrio'])

        # Deleting field 'Inmueble.titulo'
        db.delete_column(u'inmueble_inmueble', 'titulo')

        # Adding field 'Inmueble.barrio'
        db.add_column(u'inmueble_inmueble', 'barrio',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['inmueble.Barrio']),
                      keep_default=False)

        # Adding field 'Inmueble.direccion'
        db.add_column(u'inmueble_inmueble', 'direccion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'DireccionInmueble'
        db.create_table(u'inmueble_direccioninmueble', (
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.PROTECT)),
            ('inmueble', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.Inmueble'])),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True, on_delete=models.PROTECT)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, on_delete=models.PROTECT)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'inmueble', ['DireccionInmueble'])

        # Deleting model 'Barrio'
        db.delete_table(u'inmueble_barrio')

        # Adding field 'Inmueble.titulo'
        db.add_column(u'inmueble_inmueble', 'titulo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Deleting field 'Inmueble.barrio'
        db.delete_column(u'inmueble_inmueble', 'barrio_id')

        # Deleting field 'Inmueble.direccion'
        db.delete_column(u'inmueble_inmueble', 'direccion')


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
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Inmueble']"})
        },
        u'inmueble.inmueble': {
            'Meta': {'object_name': 'Inmueble'},
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Barrio']"}),
            'comodidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Comodidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 27, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inmueble']