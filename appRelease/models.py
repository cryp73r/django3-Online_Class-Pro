from django.db import models

# Create your models here.
class AppRelease(models.Model):
    ver = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    releaseDate = models.DateField()
    appFile = models.FileField(upload_to='release/')

    def __str__(self):
        return self.ver + ' ' + self.size