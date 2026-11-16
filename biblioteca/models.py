from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=20)
    anio_nacimiento = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
        titulo = models.CharField(max_length=100)
        isbn = models.CharField(unique=True, max_length=20)
        anio_publicacion = models.IntegerField()

        autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='autor')

        class Meta:
            verbose_name_plural = 'Libros'
            ordering = ['titulo']

        def __str__(self):
            return self.titulo