from django.db import models


class Blog(models.Model):
    """ Описание полей модели Blog"""

    name = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    count_views = models.SmallIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
