from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL-идентификатор'
    )
    description = HTMLField(
        blank=True,
        verbose_name='Описание'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Product(models.Model):
    order = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL-идентификатор'
    )
    description = HTMLField(
        blank=True,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['order']

    def __str__(self):
        return self.name