# Generated by Django 4.0.3 on 2022-03-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=10, verbose_name='Titulo')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('descripcion', models.CharField(max_length=250, null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
