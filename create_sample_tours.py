import os
import django
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usatavel.settings')
django.setup()

from tours.models import Tour

Tour.objects.all().delete()


sample_tours = [
    {
        'name': 'Нью-Йорк: Классический тур',
        'description': '5 дней в самом сердце Манхэттена: Таймс-сквер, Центральный парк, Бруклинский мост, Музей современного искусства',
        'image_url': 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=600&q=80',
        'price': 1499.99,
        'duration': 5,
        'popularity': 95,
        'tags': 'город, культура, музеи, шопинг, архитектура',
        'destination_type': 'ny',
    },
    {
        'name': 'Запад США: Лас-Вегас и Гранд-Каньон',
        'description': '7 дней роскоши и приключений: лучшие шоу Вегаса, вертолётный тур над каньоном, ночь в палаточном лагере у края пропасти',
        'image_url': 'https://images.unsplash.com/photo-1564325724739-bae0bd4dfc8d?auto=format&fit=crop&w=600&q=80',
        'price': 1799.99,
        'duration': 7,
        'popularity': 92,
        'tags': 'развлечения, природа, роскошь, приключения, фотографии',
        'destination_type': 'west',
    },
    {
        'name': 'Флорида: Диснейленд + Майами',
        'description': 'Волшебство Диснейленда для всей семьи + неделя на пляжах Майами. Включены все парки развлечений Орландо',
        'image_url': 'https://images.unsplash.com/photo-1529514915428-3c3856c6d1ab?auto=format&fit=crop&w=600&q=80',
        'price': 2100.00,
        'duration': 10,
        'popularity': 88,
        'tags': 'семейный, развлечения, пляж, парки аттракционов, отдых',
        'destination_type': 'fl',
    },
    {
        'name': 'Калифорния: Сан-Франциско и Лос-Анджелес',
        'description': '10 дней по Золотому штату: мост Золотые Ворота, Голливуд, Беверли-Хиллз, Силиконовая долина и винодельни Напа',
        'image_url': 'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=600&q=80',
        'price': 1950.50,
        'duration': 10,
        'popularity': 90,
        'tags': 'город, вино, пляж, технологии, кино',
        'destination_type': 'west',
    },
    {
        'name': 'Аляска: Северное сияние',
        'description': 'Уникальный тур за полярный круг: наблюдение за северным сиянием, ледники, киты и культура инуитов',
        'image_url': 'https://images.unsplash.com/photo-1502920514313-52581002a659?auto=format&fit=crop&w=600&q=80',
        'price': 3200.00,
        'duration': 8,
        'popularity': 78,
        'tags': 'природа, экзотика, приключения, фотографии, уникальное',
        'destination_type': 'custom',
    },
    {
        'name': 'Техас: Ковбои и космос',
        'description': 'Автопутешествие по Техасу: ранчо ковбоев, космический центр NASA в Хьюстоне, Остин - музыкальная столица',
        'image_url': 'https://images.unsplash.com/photo-1534040385115-33dcb3acba5b?auto=format&fit=crop&w=600&q=80',
        'price': 1650.00,
        'duration': 9,
        'popularity': 75,
        'tags': 'ковбои, космос, музыка, автопутешествие, история',
        'destination_type': 'west',
    },
    {
        'name': 'Вашингтон DC: Политика и история',
        'description': 'Экскурсия по столице США: Белый дом, Капитолий, музеи Смитсоновского института, мемориалы',
        'image_url': 'https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=600&q=80',
        'price': 1350.00,
        'duration': 4,
        'popularity': 82,
        'tags': 'история, политика, музеи, образование, архитектура',
        'destination_type': 'custom',
    },
    {
        'name': 'Гавайи: Райский отдых',
        'description': '12 дней на тропических островах: вулканы, водопады, сёрфинг, традиционная луау и пляжи с белым песком',
        'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=600&q=80',
        'price': 2800.00,
        'duration': 12,
        'popularity': 85,
        'tags': 'пляж, отдых, экзотика, вулканы, сёрфинг',
        'destination_type': 'custom',
    },
]

created_count = 0
for tour_data in sample_tours:
    tour, created = Tour.objects.get_or_create(
        name=tour_data['name'],
        defaults=tour_data
    )
    if created:
        created_count += 1
        print(f"✓ Создан тур: {tour_data['name']}")
    else:
        print(f"➤ Тур уже существует: {tour_data['name']}")

print(f"\n✅ Готово! Создано {created_count} новых туров.")
print(f"Всего туров в базе: {Tour.objects.count()}")