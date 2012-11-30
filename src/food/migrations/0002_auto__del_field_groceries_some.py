# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Groceries.some'
        db.delete_column('food_groceries', 'some')


    def backwards(self, orm):
        # Adding field 'Groceries.some'
        db.add_column('food_groceries', 'some',
                      self.gf('django.db.models.fields.FloatField')(default='0.1'),
                      keep_default=False)


    models = {
        'food.groceries': {
            'Meta': {'object_name': 'Groceries'},
            'carbohydrates': ('django.db.models.fields.FloatField', [], {}),
            'energy': ('django.db.models.fields.FloatField', [], {}),
            'fats': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proteins': ('django.db.models.fields.FloatField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['food']