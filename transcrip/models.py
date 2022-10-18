from django.db import models

# Create your models here.

class Transcrip(models.Model):
    '''
    Modelo de clase del objeto transcrip que contiene las transcriptiones \n
    researcher - string \n
    date - dateType \n
    duration - float \n
    location - string
    '''
    def __str__(self):
        return self.code
    code = models.CharField(max_length=50, primary_key=True)
    city = models.CharField(max_length=100, default="Desconocido")
    country = models.CharField(max_length=100, default="Desconocido")
    descrip = models.FileField(upload_to='pdf_files')
    transcrip = models.FileField(upload_to='pdf_files')
    audio = models.FileField(upload_to='audio_files')