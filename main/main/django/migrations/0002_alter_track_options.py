# Generated by Django 5.1 on 2024-08-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['track_order']},
        ),
    ]
