# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Servicio.descripcion'
        db.alter_column(u'inmueble_servicio', 'descripcion', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=60))
        # Adding unique constraint on 'Servicio', fields ['descripcion']
        db.create_unique(u'inmueble_servicio', ['descripcion'])


        # Changing field 'Inmueble.precio_semana'
        db.alter_column(u'inmueble_inmueble', 'precio_semana', self.gf('django.db.models.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'Inmueble.precio_mes'
        db.alter_column(u'inmueble_inmueble', 'precio_mes', self.gf('django.db.models.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'Inmueble.tipo_inmueble'
        db.alter_column(u'inmueble_inmueble', 'tipo_inmueble_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.TipoInmueble'], null=True))

        # Changing field 'Inmueble.descripcion'
        db.alter_column(u'inmueble_inmueble', 'descripcion', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Inmueble.titulo'
        db.alter_column(u'inmueble_inmueble', 'titulo', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Inmueble.precio_dia'
        db.alter_column(u'inmueble_inmueble', 'precio_dia', self.gf('django.db.models.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'Comodidad.descripcion'
        db.alter_column(u'inmueble_comodidad', 'descripcion', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=60))
        # Adding unique constraint on 'Comodidad', fields ['descripcion']
        db.create_unique(u'inmueble_comodidad', ['descripcion'])


        # Changing field 'TipoInmueble.descripcion'
        db.alter_column(u'inmueble_tipoinmueble', 'descripcion', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=60))
        # Adding unique constraint on 'TipoInmueble', fields ['descripcion']
        db.create_unique(u'inmueble_tipoinmueble', ['descripcion'])


    def backwards(self, orm):
        # Removing unique constraint on 'TipoInmueble', fields ['descripcion']
        db.delete_unique(u'inmueble_tipoinmueble', ['descripcion'])

        # Removing unique constraint on 'Comodidad', fields ['descripcion']
        db.delete_unique(u'inmueble_comodidad', ['descripcion'])

        # Removing unique constraint on 'Servicio', fields ['descripcion']
        db.delete_unique(u'inmueble_servicio', ['descripcion'])


        # Changing field 'Servicio.descripcion'
        db.alter_column(u'inmueble_servicio', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Inmueble.precio_semana'
        db.alter_column(u'inmueble_inmueble', 'precio_semana', self.gf('django.db.models.DecimalField')(default=0, max_digits=8, decimal_places=2))

        # Changing field 'Inmueble.precio_mes'
        db.alter_column(u'inmueble_inmueble', 'precio_mes', self.gf('django.db.models.DecimalField')(default=0, max_digits=8, decimal_places=2))

        # Changing field 'Inmueble.tipo_inmueble'
        db.alter_column(u'inmueble_inmueble', 'tipo_inmueble_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['inmueble.TipoInmueble']))

        # Changing field 'Inmueble.descripcion'
        db.alter_column(u'inmueble_inmueble', 'descripcion', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Inmueble.titulo'
        db.alter_column(u'inmueble_inmueble', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Inmueble.precio_dia'
        db.alter_column(u'inmueble_inmueble', 'precio_dia', self.gf('django.db.models.DecimalField')(default=0, max_digits=8, decimal_places=2))

        # Changing field 'Comodidad.descripcion'
        db.alter_column(u'inmueble_comodidad', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'TipoInmueble.descripcion'
        db.alter_column(u'inmueble_tipoinmueble', 'descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

    models = {
        u'cities_light.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'cities_light.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'cities_light.region': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'inmueble.comodidad': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Comodidad'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.direccioninmueble': {
            'Meta': {'object_name': 'DireccionInmueble'},
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Inmueble']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True', 'on_delete': 'models.PROTECT'})
        },
        u'inmueble.fotoinmueble': {
            'Meta': {'object_name': 'FotoInmueble'},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Inmueble']"})
        },
        u'inmueble.inmueble': {
            'Meta': {'object_name': 'Inmueble'},
            'comodidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Comodidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 27, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_dia': ('django.db.models.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'precio_mes': ('django.db.models.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'precio_semana': ('django.db.models.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {}),
            'servicios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Servicio']", 'symmetrical': 'False', 'blank': 'True'}),
            'superficie': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.TipoInmueble']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
