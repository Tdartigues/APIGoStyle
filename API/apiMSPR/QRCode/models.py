from django.db import models
from django.core.exceptions import ValidationError
import uuid

# Create your models here.

def validate_taux(value):
    if (value >= 1 and value <= 100):
        return value
    else:
        raise ValidationError("Taux must be between 1 and 100")

class Reduction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=128)
    taux = models.PositiveIntegerField(validators = [validate_taux])

    def __str__(self):
            return f"{self.nom} {self.taux} % [{self.id}]"

    class Meta:
        ordering = ['nom', 'taux']