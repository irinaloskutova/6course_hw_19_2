from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    picture = models.ImageField(upload_to='products/', verbose_name="Изображение (превью)", **NULLABLE)
    category = models.CharField(max_length=150, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена за покупку")
    creation_date = models.DateField(auto_now=False, verbose_name="Дата создания")
    last_modified_date = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Дата последнего"
                                                                                          " изменения")

    def __str__(self):
        return f'{self.name_product} - {self.description} в категории: {self.category}, цена: {self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f'{self.name} - {self.description}'
