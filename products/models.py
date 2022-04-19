from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='название', max_length=256)
    image = models.ImageField(verbose_name='изображение', upload_to='products_images', blank=True)
    description = models.CharField(verbose_name='описание', max_length=256)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    category = models.ForeignKey(ProductCategory, verbose_name='категория', on_delete=models.CASCADE)
    discount = models.PositiveIntegerField(verbose_name='скидка', default=0)
    discount_price = models.DecimalField(verbose_name='цена со скидкой', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category}'
