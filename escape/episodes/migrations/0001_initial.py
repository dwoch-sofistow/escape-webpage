# Generated by Django 2.1.5 on 2019-02-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pubdate', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('video', models.CharField(max_length=500)),
                ('skin1', models.ImageField(blank=True, null=True, upload_to='images')),
                ('skin2', models.ImageField(blank=True, null=True, upload_to='images')),
                ('resource1', models.TextField()),
                ('resource2', models.TextField()),
                ('link', models.TextField()),
                ('censorlink', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HiddenEpisode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pubdate', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('video', models.CharField(max_length=500)),
                ('skin', models.ImageField(blank=True, null=True, upload_to='images')),
                ('resource1', models.TextField()),
                ('resource2', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
