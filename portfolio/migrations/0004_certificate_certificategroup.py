# Generated by Django 3.0.7 on 2020-08-02 11:36

from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200802_0710'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to=portfolio.models.image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificates', to='portfolio.CertificateGroup')),
            ],
        ),
    ]
