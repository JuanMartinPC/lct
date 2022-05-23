from email.policy import default
from django.db import models


class Empresas(models.TextChoices):
    Natura = 'Natura', 'Natura',
    Millanel = 'Millanel', 'Millanel',
    Tupper = 'Tupper','Tupper',
    Winnem = 'Winnem','Winnem',
    Avon = 'Avon','Avon',
    MeryKay = 'MeryKay','MeryKay',

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nombre")
    codigo = models.CharField(max_length=255, blank=False, null=False, verbose_name="Código")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    precio = models.IntegerField(default=0, verbose_name="Precio")
    descripcion = models.CharField(max_length=255, blank=True, null=False, default='', verbose_name="Descripción")
    img = models.ImageField(upload_to="AliciaPage\static\imagenes", null=True, verbose_name="Imagen", default=r'AliciaPage\static\imagenes\default.jpg')
    empresa = models.CharField(choices= Empresas.choices, max_length=8, default= Empresas.Natura)

    def delete(self):
        self.img.storage.delete(self.img.name)
        super().delete()
