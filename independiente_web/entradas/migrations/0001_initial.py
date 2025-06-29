# Generated by Django 5.2.3 on 2025-06-14 00:30

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaPartido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(upload_to='entradas/')),
                ('fecha', models.DateField()),
                ('comprador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
