from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Слаг', unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class SubCategory(models.Model):

    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name='Назва', unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Слаг', unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Підкатегорія'
        verbose_name_plural = 'Підкатегорії'
