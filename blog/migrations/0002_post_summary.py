# Generated by Django 3.0.5 on 2020-05-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(default='Summary of the post', max_length=500),
            preserve_default=False,
        ),
    ]
