from django.db import models


class BasePublishableModel(models.Model):
    """Абстрактная модель, добавляющая флаг публикации и автоматическое
    сохранение времени создания записи.

    Атрибуты:
        is_published (BooleanField): Флаг, указывающий на публикацию записи.
            Значение по умолчанию — True.
            Если снять галочку, публикация будет скрыта.
        created_at (DateTimeField): Время создания записи.
            Устанавливается автоматически при добавлении записи.
    """

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True
