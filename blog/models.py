from django.db import models

# Create your models here.


class BlogEntry(models.Model):
    title = models.CharField(
                        max_length=100,
                        verbose_name='Заголовок'
                    )
    slug = models.CharField(
                        max_length=150,
                        null=True,
                        blank=True,
                        verbose_name='slug'
                    )
    content = models.TextField(
                        null=True,
                        blank=True,
                        verbose_name='Содержимое'
                    )
    image = models.ImageField(
                        default='blog/default.jpg',
                        upload_to='blog/',
                        null=True,
                        blank=True,
                        verbose_name='Изображение'
                    )
    creation_date = models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Дата создания'
                    )
    is_published = models.BooleanField(
                        default=False,
                        verbose_name='Опубликовано'
                    )
    number_views = models.PositiveIntegerField(
                        default=0,
                        verbose_name='Количество просмотров'
                    )

    def __str__(self):
        return f"{self.title, self.is_published}"

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'