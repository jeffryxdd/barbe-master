# Generated by Django 4.0.1 on 2022-05-24 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('idTipoServicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreTipoServicio', models.CharField(max_length=50, verbose_name='Tipo de Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Servicio')),
                ('nombreServicio', models.CharField(max_length=50, verbose_name='Nombre Servicio')),
                ('img', models.ImageField(default='', upload_to='users/static/barb/img/', verbose_name='Imagen Servicio')),
                ('descripcionServicio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción Servicio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.tiposervicio')),
            ],
        ),
    ]
