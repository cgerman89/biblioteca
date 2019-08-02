# Generated by Django 2.2.3 on 2019-08-02 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'books"."autor',
                'ordering': ['name'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titulo')),
                ('date_published', models.DateField(auto_now_add=True, verbose_name='Fecha Publicado')),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'db_table': 'books"."libro',
                'ordering': ['title'],
                'managed': True,
            },
        ),
    ]