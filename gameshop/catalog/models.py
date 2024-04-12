from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.URLField('Изображение')
    price = models.IntegerField('Цена')
    is_available = models.BooleanField(verbose_name='Наличие', default=True)
    slug = models.SlugField(unique=True, default='')
    cat = models.ManyToManyField(ProductCategory, verbose_name='Категория')

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog-detail", kwargs={"slug": self.slug})


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар', null=False)
    review = models.TextField(verbose_name='Текст отзыва', max_length=400)
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None, verbose_name='Оценка')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.user}, {self.product}, Оценка: {self.rating}, Дата: {self.date}'
