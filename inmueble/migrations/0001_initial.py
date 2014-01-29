# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoInmueble'
        db.create_table(u'inmueble_tipoinmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
        ))
        db.send_create_signal(u'inmueble', ['TipoInmueble'])

        # Adding model 'Comodidad'
        db.create_table(u'inmueble_comodidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
        ))
        db.send_create_signal(u'inmueble', ['Comodidad'])

        # Adding model 'Servicio'
        db.create_table(u'inmueble_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
        ))
        db.send_create_signal(u'inmueble', ['Servicio'])

        # Adding model 'Inmueble'
        db.create_table(u'inmueble_inmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tipo_inmueble', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.TipoInmueble'])),
            ('superficie', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('precio_dia', self.gf('django.db.models.DecimalField')(max_digits=8, decimal_places=2)),
            ('precio_semana', self.gf('django.db.models.DecimalField')(max_digits=8, decimal_places=2)),
            ('precio_mes', self.gf('django.db.models.DecimalField')(max_digits=8, decimal_places=2)),
            ('publicado', self.gf('django.db.models.fields.BooleanField')()),
            ('destacado', self.gf('django.db.models.fields.BooleanField')()),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 27, 0, 0))),
        ))
        db.send_create_signal(u'inmueble', ['Inmueble'])

        # Adding M2M table for field comodidades on 'Inmueble'
        m2m_table_name = db.shorten_name(u'inmueble_inmueble_comodidades')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inmueble', models.ForeignKey(orm[u'inmueble.inmueble'], null=False)),
            ('comodidad', models.ForeignKey(orm[u'inmueble.comodidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['inmueble_id', 'comodidad_id'])

        # Adding M2M table for field servicios on 'Inmueble'
        m2m_table_name = db.shorten_name(u'inmueble_inmueble_servicios')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inmueble', models.ForeignKey(orm[u'inmueble.inmueble'], null=False)),
            ('servicio', models.ForeignKey(orm[u'inmueble.servicio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['inmueble_id', 'servicio_id'])

        # Adding model 'DireccionInmueble'
        db.create_table(u'inmueble_direccioninmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True, on_delete=models.PROTECT)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True, on_delete=models.PROTECT)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, on_delete=models.PROTECT)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('inmueble', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.Inmueble'])),
        ))
        db.send_create_signal(u'inmueble', ['DireccionInmueble'])

        # Adding model 'FotoInmueble'
        db.create_table(u'inmueble_fotoinmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inmueble', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.Inmueble'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'inmueble', ['FotoInmueble'])


    def backwards(self, orm):
        # Deleting model 'TipoInmueble'
        db.delete_table(u'inmueble_tipoinmueble')

        # Deleting model 'Comodidad'
        db.delete_table(u'inmueble_comodidad')

        # Deleting model 'Servicio'
        db.delete_table(u'inmueble_servicio')

        # Deleting model 'Inmueble'
        db.delete_table(u'inmueble_inmueble')

        # Removing M2M table for field comodidades on 'Inmueble'
        db.delete_table(db.shorten_name(u'inmueble_inmueble_comodidades'))

        # Removing M2M table for field servicios on 'Inmueble'
        db.delete_table(db.shorten_name(u'inmueble_inmueble_servicios'))

        # Deleting model 'DireccionInmueble'
        db.delete_table(u'inmueble_direccioninmueble')

        # Deleting model 'FotoInmueble'
        db.delete_table(u'inmueble_fotoinmueble')


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
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'db_index': 'True', 'blank': 'True'}),
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
            'Meta': {'object_name': 'Comodidad'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
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
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 27, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_dia': ('django.db.models.DecimalField', [], {'currency': "'USD'", 'max_digits': '8', 'decimal_places': '2'}),
            'precio_mes': ('django.db.models.DecimalField', [], {'currency': "'USD'", 'max_digits': '8', 'decimal_places': '2'}),
            'precio_semana': ('django.db.models.DecimalField', [], {'currency': "'USD'", 'max_digits': '8', 'decimal_places': '2'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {}),
            'servicios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Servicio']", 'symmetrical': 'False', 'blank': 'True'}),
            'superficie': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.TipoInmueble']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'inmueble.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.tipoinmueble': {
            'Meta': {'object_name': 'TipoInmueble'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inmueble']