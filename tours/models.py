from django.db import models
from django.utils.translation import gettext_lazy as _

class Tour(models.Model):
    DURATION_CHOICES = [
        (5, '5 дней'),
        (7, '7 дней'),
        (10, '10 дней'),
        (14, '14 дней'),
        (21, '21 день'),
    ]
    
    name = models.CharField(_('Название'), max_length=200)
    description = models.TextField(_('Описание'))
    image_url = models.URLField(_('URL изображения'))
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    duration = models.IntegerField(_('Длительность'), choices=DURATION_CHOICES)
    popularity = models.IntegerField(_('Популярность'), default=0)
    tags = models.CharField(_('Теги'), max_length=500, help_text=_('Разделяйте теги запятой'))
    destination_type = models.CharField(_('Тип направления'), max_length=50, choices=[
        ('ny', 'Нью-Йорк'),
        ('west', 'Запад США'),
        ('fl', 'Флорида'),
        ('custom', 'Индивидуальный'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Тур')
        verbose_name_plural = _('Туры')
    
    def __str__(self):
        return self.name
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',')]