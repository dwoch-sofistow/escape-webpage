# Generated by Django 2.1.5 on 2019-02-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiddenresource',
            name='file',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='file',
            field=models.TextField(blank=True, null=True),
        ),
    ]
