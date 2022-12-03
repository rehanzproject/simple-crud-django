from django.db import models

# Create your models here.
class Tabel(models.Model):
    nama = models.CharField(max_length=30)
    kelas = models.CharField(max_length=10)
    matkul = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

    