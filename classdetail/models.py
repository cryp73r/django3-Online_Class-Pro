from django.db import models

# Create your models here.
# For CS 3334
class classdetailcs3334(models.Model):
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    subteach = models.CharField(max_length=60, default='N/A')
    classgroup = models.CharField(max_length=4, default='3334')
    url = models.URLField(blank=True)
    meetid = models.CharField(max_length=13, blank=True)
    password = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title + ' ' + self.classgroup

# For CS 3132
class classdetailcs3132(models.Model):
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    subteach = models.CharField(max_length=60, default='N/A')
    classgroup = models.CharField(max_length=4, default='3132')
    url = models.URLField(blank=True)
    meetid = models.CharField(max_length=13, blank=True)
    password = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title + ' ' + self.classgroup

# For CS 4142
class classdetailcs4142(models.Model):
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    subteach = models.CharField(max_length=60, default='N/A')
    classgroup = models.CharField(max_length=4, default='4142')
    url = models.URLField(blank=True)
    meetid = models.CharField(max_length=13, blank=True)
    password = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title + ' ' + self.classgroup

# For CS 4344
class classdetailcs4344(models.Model):
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    subteach = models.CharField(max_length=60, default='N/A')
    classgroup = models.CharField(max_length=4, default='4344')
    url = models.URLField(blank=True)
    meetid = models.CharField(max_length=13, blank=True)
    password = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title + ' ' + self.classgroup

# For CS 45
class classdetailcs45(models.Model):
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    subteach = models.CharField(max_length=60, default='N/A')
    classgroup = models.CharField(max_length=4, default='45')
    url = models.URLField(blank=True)
    meetid = models.CharField(max_length=13, blank=True)
    password = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title + ' ' + self.classgroup

# For IT 4142
class classdetailit4142(models.Model):
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    subteach = models.CharField(max_length=60, default='N/A')
    classgroup = models.CharField(max_length=4, default='4142')
    url = models.URLField(blank=True)
    meetid = models.CharField(max_length=13, blank=True)
    password = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title + ' ' + self.classgroup

# For IT 4344
class classdetailit4344(models.Model):
    title = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    subteach = models.CharField(max_length=60, default='N/A')
    classgroup = models.CharField(max_length=4, default='4344')
    url = models.URLField(blank=True)
    meetid = models.CharField(max_length=13, blank=True)
    password = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title + ' ' + self.classgroup