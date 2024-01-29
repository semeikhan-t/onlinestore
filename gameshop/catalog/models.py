from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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
    cat = models.ManyToManyField(ProductCategory, null=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
