# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Food'
        db.create_table('food_food', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('energy', self.gf('django.db.models.fields.FloatField')()),
            ('proteins', self.gf('django.db.models.fields.FloatField')()),
            ('fats', self.gf('django.db.models.fields.FloatField')()),
            ('carbohydrates', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('food', ['Food'])

        # Adding model 'Portion'
        db.create_table('food_portion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Food'])),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('food', ['Portion'])


    def backwards(self, orm):
        # Deleting model 'Food'
        db.delete_table('food_food')

        # Deleting model 'Portion'
        db.delete_table('food_portion')


    models = {
        'food.food': {
            'Meta': {'object_name': 'Food'},
            'carbohydrates': ('django.db.models.fields.FloatField', [], {}),
            'energy': ('django.db.models.fields.FloatField', [], {}),
            'fats': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proteins': ('django.db.models.fields.FloatField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'food.portion': {
            'Meta': {'object_name': 'Portion'},
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['food.Food']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['food']