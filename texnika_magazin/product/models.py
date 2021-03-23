from django.db import models

from django.db import models


def default_info():
    return {
        "information": [
            {
                "title": "",
                "value": ""
            }
        ]
    }


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = (('name', 'category'), )

    def __str__(self):
        return self.name


class BrandModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = (('name', 'brand'), )

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.CharField(max_length=500, blank=False, null=False)
    price = models.BigIntegerField(blank=False, null=False)
    info = models.JSONField(blank=False, null=False, default=default_info())
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.SET_NULL)
    model = models.ForeignKey(BrandModel, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
