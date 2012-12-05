# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Store', fields ['user', 'name']
        db.delete_unique('stores_store', ['user_id', 'name'])

        # Deleting field 'Store.user'
        db.delete_column('stores_store', 'user_id')

        # Adding unique constraint on 'Store', fields ['name']
        db.create_unique('stores_store', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Store', fields ['name']
        db.delete_unique('stores_store', ['name'])


        # User chose to not deal with backwards NULL issues for 'Store.user'
        raise RuntimeError("Cannot reverse this migration. 'Store.user' and its values cannot be restored.")
        # Adding unique constraint on 'Store', fields ['user', 'name']
        db.create_unique('stores_store', ['user_id', 'name'])


    models = {
        'stores.store': {
            'Meta': {'ordering': "['name']", 'object_name': 'Store'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        }
    }

    complete_apps = ['stores']