from django.db import models

# Create your models here.
DEPARTMENT_CHOICE = (
    ('Computer Science & Engineering', 'Computer Science & Engineering'),
    ('Information Technology', 'Information Technology')
)

class Quiz(models.Model):
    Subject = models.CharField(max_length=100)
    SubCode = models.CharField(max_length=10)
    Department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICE)
    Date = models.DateField()
    Url = models.URLField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.Subject + ' ' + self.Department