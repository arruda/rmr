# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Author', fields ['user', 'name']
        db.delete_unique('authors_author', ['user_id', 'name'])

        # Deleting field 'Author.user'
        db.delete_column('authors_author', 'user_id')

        # Adding unique constraint on 'Author', fields ['name']
        db.create_unique('authors_author', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Author', fields ['name']
        db.delete_unique('authors_author', ['name'])


        # User chose to not deal with backwards NULL issues for 'Author.user'
        raise RuntimeError("Cannot reverse this migration. 'Author.user' and its values cannot be restored.")
        # Adding unique constraint on 'Author', fields ['user', 'name']
        db.create_unique('authors_author', ['user_id', 'name'])


    models = {
        'authors.author': {
            'Meta': {'ordering': "['name']", 'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        }
    }

    complete_apps = ['authors']