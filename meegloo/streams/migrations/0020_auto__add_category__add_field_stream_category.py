# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('streams_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True))
        ))
        db.send_create_signal('streams', ['Category'])
        db.add_column('streams_category', 'parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['streams.Category'], null=True))

        # Adding field 'Stream.category'
        db.add_column('streams_stream', 'category', self.gf('django.db.models.fields.related.ForeignKey')(default=5, related_name='streams', to=orm['streams.Category']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('streams_category')

        # Deleting field 'Stream.category'
        db.delete_column('streams_stream', 'category_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'networks.network': {
            'Meta': {'ordering': "('-featured', 'name')", 'object_name': 'Network'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'managers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'managed_networks'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_networks'", 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': "orm['networks.SuperNetwork']"}),
            'privacy': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'networks.supernetwork': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SuperNetwork'},
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'piston.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '16'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'consumers'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'social.comment': {
            'Meta': {'ordering': "('-posted',)", 'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['auth.User']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['networks.Network']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'posted': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'tweet': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'streams.category': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['streams.Category']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'streams.conversion': {
            'Meta': {'ordering': "('updated',)", 'object_name': 'Conversion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conversions'", 'to': "orm['streams.Post']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'streams.embeddable': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('post', 'url'),)", 'object_name': 'Embeddable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'embeddables'", 'to': "orm['streams.Post']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'streams.media': {
            'Meta': {'ordering': "('post', 'content')", 'unique_together': "(('post', 'mimetype'),)", 'object_name': 'Media'},
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': "orm['streams.Post']"})
        },
        'streams.post': {
            'Meta': {'ordering': "('-posted',)", 'object_name': 'Post'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'posts'", 'null': 'True', 'to': "orm['piston.Consumer']"}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'posts'", 'null': 'True', 'to': "orm['auth.User']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['streams.UserStream']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tweet': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'streams.set': {
            'Meta': {'ordering': "('posted',)", 'object_name': 'Set'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sets'", 'null': 'True', 'to': "orm['piston.Consumer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sets'", 'symmetrical': 'False', 'to': "orm['streams.Post']"}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sets'", 'to': "orm['streams.UserStream']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'streams.stream': {
            'Meta': {'ordering': "('-updated',)", 'object_name': 'Stream'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '5', 'related_name': "'streams'", 'to': "orm['streams.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'streams'", 'to': "orm['networks.Network']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'streams.streamembed': {
            'Meta': {'ordering': "('domain',)", 'unique_together': "(('stream', 'domain'),)", 'object_name': 'StreamEmbed', 'db_table': "'streams_stream_embed'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'embeds'", 'to': "orm['streams.UserStream']"})
        },
        'streams.streamtag': {
            'Meta': {'unique_together': "(('stream', 'user', 'domain', 'tag'),)", 'object_name': 'StreamTag', 'db_table': "'streams_stream_tag'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': "orm['streams.Stream']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stream_tags'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'streams.trend': {
            'Meta': {'ordering': "('-time', '-posts')", 'object_name': 'Trend'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trends'", 'to': "orm['streams.Stream']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'streams.userstream': {
            'Meta': {'ordering': "('-updated',)", 'object_name': 'UserStream', 'db_table': "'streams_stream_user'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part_of': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contributors'", 'to': "orm['streams.Stream']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'streams'", 'to': "orm['auth.User']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['streams']
