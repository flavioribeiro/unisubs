# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding M2M table for field videos on 'CustomUser'
        db.create_table('auth_customuser_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm['auth.customuser'], null=False)),
            ('video', models.ForeignKey(orm['videos.video'], null=False))
        ))
        db.create_unique('auth_customuser_videos', ['customuser_id', 'video_id'])
    
    
    def backwards(self, orm):
        
        # Removing M2M table for field videos on 'CustomUser'
        db.delete_table('auth_customuser_videos')
    
    
    models = {
        'auth.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'auth.awards': {
            'Meta': {'object_name': 'Awards'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.CustomUser']", 'null': 'True'})
        },
        'auth.customuser': {
            'Meta': {'object_name': 'CustomUser', '_ormbases': ['auth.User']},
            'autoplay_preferences': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'award_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'changes_notification': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'last_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'picture': ('utils.amazon.fields.S3EnabledImageField', [], {'max_length': '100', 'blank': 'True'}),
            'preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'valid_email': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['videos.Video']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.message': {
            'Meta': {'object_name': 'Message'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_message_set'", 'to': "orm['auth.User']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'auth.userlanguage': {
            'Meta': {'unique_together': "(['user', 'language'],)", 'object_name': 'UserLanguage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'proficiency': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.CustomUser']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'videos.video': {
            'Meta': {'object_name': 'Video'},
            'allow_community_edits': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'allow_video_urls_edit': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'complete_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edited': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'followed_videos'", 'blank': 'True', 'to': "orm['auth.CustomUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_subtitled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'languages_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            's3_thumbnail': ('utils.amazon.fields.S3EnabledImageField', [], {'max_length': '100', 'blank': 'True'}),
            'subtitles_fetched_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.CustomUser']", 'null': 'True', 'blank': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'was_subtitled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'widget_views_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'writelock_owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'writelock_owners'", 'null': 'True', 'to': "orm['auth.CustomUser']"}),
            'writelock_session_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'writelock_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }
    
    complete_apps = ['auth']
