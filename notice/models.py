from django.db import models

# Create your models here.
class Notice(models.Model):
    department = models.CharField(max_length=60)
    designation = models.CharField(max_length=30)
    signatory = models.CharField(max_length=30)
    date = models.DateField()
    message = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.department + ' ' + str(self.date)