from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name


