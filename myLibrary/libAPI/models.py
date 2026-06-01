from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Autor(BaseModel):
    nombre = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField()

class VisualNovel(BaseModel):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    dificultad = models.DecimalField(max_digits=2, decimal_places=2)
    fecha_creacion = models.DateField()



