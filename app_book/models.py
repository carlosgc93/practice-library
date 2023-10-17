from django.db import models
from django.utils.timezone import *


# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre',max_length=200, blank=False, null=False)
    last_name = models.CharField('Apellidos',max_length=220, blank=False, null=False)
    nationality = models.CharField('Nacionalidad',max_length=100, blank=False, null=False)
    description_author = models.TextField('Bio',blank=False, null=False)
    status_author = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=255, blank=False, null=False)
    publication_date = models.DateField(
        'Fecha de publicación', blank=False, null=False)
    author_id = models.ManyToManyField(Author)
    description_book = models.TextField('Descripción')
    creation_date_book = models.DateTimeField(
        'Fecha de creación', auto_now_add=True)
    front_page = models.ImageField(upload_to='front_images',null=False, blank=False )

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['id']

    def __str__(self):
        return self.title
