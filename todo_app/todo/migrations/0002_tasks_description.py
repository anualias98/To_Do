# Generated by Django 4.1.6 on 2023-02-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
