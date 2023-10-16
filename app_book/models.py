from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=220, blank=False, null=False)
    nationality = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status_author = models.BooleanField('Estado', default=True)
    creation_date = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=255, blank=False, null=False)
    publication_date = models.DateField('Fecha de publicación', blank=False, null=False)
    author_id = models.ManyToManyField(Author)
    creation_date_book = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['id']

    def __str__(self):
        return self.title
