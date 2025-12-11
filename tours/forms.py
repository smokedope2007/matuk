from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Tour

class BookingForm(forms.Form):
    name = forms.CharField(
        label=_('Ваше имя'),
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _('Ваше имя'),
            'aria-label': _('Ваше имя'),
        })
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs={
            'placeholder': _('Email'),
            'aria-label': _('Email'),
        })
    )
    
    # Динамически получаем направления из БД
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Получаем уникальные типы направлений из базы
        tour_types = Tour.objects.values_list('destination_type', 'name').distinct()
        
        choices = [('', _('Выберите направление'))]
        
        # Добавляем направления из БД
        for dest_type, name in tour_types:
            display_name = dict(Tour._meta.get_field('destination_type').choices).get(dest_type, dest_type)
            choices.append((dest_type, display_name))
        
        # Добавляем индивидуальный маршрут
        choices.append(('custom', _('Индивидуальный маршрут')))
        
        self.fields['destination'] = forms.ChoiceField(
            label=_('Направление'),
            choices=choices,
            required=True,
            widget=forms.Select(attrs={'aria-label': _('Выберите направление')})
        )
    
    travel_date = forms.DateField(
        label=_('Дата начала тура'),
        widget=forms.DateInput(attrs={
            'type': 'date',
            'aria-label': _('Дата начала тура'),
        })
    )
    
    participants = forms.IntegerField(
        label=_('Количество участников'),
        min_value=1,
        max_value=20,
        initial=2,
        widget=forms.NumberInput(attrs={
            'placeholder': _('Количество участников'),
            'aria-label': _('Количество участников'),
        })
    )