from django.db import models


# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False)
    lastname = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(blank=False, max_length=200, null=False, verbose_name='Descripcion')
    date_create = models.DateField('Fecha Creacion', auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'books\".\"autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['name']

    def __str__(self):
        return self.name


class Libro(models.Model):
    title = models.CharField('Titulo', max_length=255, blank=False, null=False)
    date_published = models.DateField('Fecha Publicado', blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    date_create = models.DateField('Fecha Creacion',auto_now=True, auto_now_add=False)

    class Meta:
        managed = True
        db_table = 'books\".\"libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']

    def __str__(self):
        return self.title
