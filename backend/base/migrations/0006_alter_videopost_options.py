# Generated by Django 4.2.7 on 2023-11-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_videopost_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videopost',
            options={'ordering': ('-updated_at', '-created_at')},
        ),
    ]