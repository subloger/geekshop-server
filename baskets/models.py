from django.db import models, transaction

from users.models import User
from products.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user).select_related('product')
        return sum(basket.sum() for basket in baskets)

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(id=pk).first()

    # переопределение метода сохранения
    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.pk:
                self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
            else:
                self.product.quantity -= self.quantity
            self.product.save()
            super(Basket, self).save(*args, **kwargs)

    # переопределение метода удаление
    @transaction.atomic
    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.product.save()
        super(Basket, self).delete(*args, **kwargs)
