# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Groceries'
        db.create_table('food_groceries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('energy', self.gf('django.db.models.fields.FloatField')()),
            ('proteins', self.gf('django.db.models.fields.FloatField')()),
            ('fats', self.gf('django.db.models.fields.FloatField')()),
            ('carbohydrates', self.gf('django.db.models.fields.FloatField')()),
            ('some', self.gf('django.db.models.fields.FloatField')(default='0.1')),
        ))
        db.send_create_signal('food', ['Groceries'])


    def backwards(self, orm):
        # Deleting model 'Groceries'
        db.delete_table('food_groceries')


    models = {
        'food.groceries': {
            'Meta': {'object_name': 'Groceries'},
            'carbohydrates': ('django.db.models.fields.FloatField', [], {}),
            'energy': ('django.db.models.fields.FloatField', [], {}),
            'fats': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proteins': ('django.db.models.fields.FloatField', [], {}),
            'some': ('django.db.models.fields.FloatField', [], {'default': "'0.1'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['food']