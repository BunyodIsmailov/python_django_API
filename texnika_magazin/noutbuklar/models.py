from django.db import models


class Aperatsion_tizim(models.Model):
    type = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.type

class Noutbuklar(models.Model):
    brend = models.CharField(max_length=50, blank=False, null=False)
    memory = models.CharField(max_length=50, blank=False, null=False)
    type = models.ForeignKey(Aperatsion_tizim, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.brend