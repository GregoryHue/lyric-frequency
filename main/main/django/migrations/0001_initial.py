# Generated by Django 5.1 on 2024-08-24 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('album_image_url', models.CharField(max_length=255)),
                ('genius_url', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('album_name', 'artist_name')},
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=255)),
                ('lyrics', models.TextField()),
                ('track_order', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='django.album')),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('track_name', 'album')},
            },
        ),
    ]
