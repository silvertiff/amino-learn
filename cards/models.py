from django.db import models

# Create your models here.
from django.db import models

class AminoAcidCard(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    structure = models.TextField(verbose_name="Строение")
    code = models.CharField(max_length=3, verbose_name="Трёхбуквенный код")
    image = models.ImageField(upload_to='amino_images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return f"{self.name} ({self.code})"

