# Generated by Django 5.0.1 on 2024-01-12 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
