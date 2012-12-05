# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Publisher', fields ['user', 'name']
        db.delete_unique('publishers_publisher', ['user_id', 'name'])

        # Deleting field 'Publisher.user'
        db.delete_column('publishers_publisher', 'user_id')

        # Adding unique constraint on 'Publisher', fields ['name']
        db.create_unique('publishers_publisher', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Publisher', fields ['name']
        db.delete_unique('publishers_publisher', ['name'])


        # User chose to not deal with backwards NULL issues for 'Publisher.user'
        raise RuntimeError("Cannot reverse this migration. 'Publisher.user' and its values cannot be restored.")
        # Adding unique constraint on 'Publisher', fields ['user', 'name']
        db.create_unique('publishers_publisher', ['user_id', 'name'])


    models = {
        'publishers.publisher': {
            'Meta': {'ordering': "['name']", 'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        }
    }

    complete_apps = ['publishers']