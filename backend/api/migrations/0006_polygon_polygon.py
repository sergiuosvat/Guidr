# Generated by Django 3.2 on 2023-05-13 11:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_sesizarefunctionar1_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='polygon',
            name='polygon',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
