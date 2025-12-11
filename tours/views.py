from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .forms import BookingForm

def home(request):
    destinations = [
        {
            'name': _('Нью-Йорк: Классический тур'),
            'description': _('5 дней в самом сердце Манхэттена: Таймс-сквер, Центральный парк, Бруклинский мост, Музей современного искусства'),
            'image_url': 'https://avatars.mds.yandex.net/i?id=50d493ce956af79a52a7f8ecc0a21611bfc95f0a507e6f20-5233063-images-thumbs&n=13',
            'price': 1499.99,
            'duration': 5,
            'popularity': 95,
            'tags': ['город', 'культура', 'музеи', 'шопинг', 'архитектура'],
            'destination_type': 'ny',
        },
        {
            'name': _('Запад США: Лас-Вегас и Гранд-Каньон'),
            'description': _('7 дней роскоши и приключений: лучшие шоу Вегаса, вертолётный тур над каньоном, ночь в палаточном лагере у края пропасти'),
            'image_url': 'https://avatars.mds.yandex.net/i?id=99ee35e1a0dd4dafc103b0d03b711d1babd2ab57-10805535-images-thumbs&n=13',
            'price': 1799.99,
            'duration': 7,
            'popularity': 92,
            'tags': ['развлечения', 'природа', 'роскошь', 'приключения', 'фотографии'],
            'destination_type': 'west',
        },
        {
            'name': _('Флорида: Диснейленд + Майами'),
            'description': _('Волшебство Диснейленда для всей семьи + неделя на пляжах Майами. Включены все парки развлечений Орландо'),
            'image_url': 'https://avatars.mds.yandex.net/i?id=19eeec533cc0724312982a84346d8d2ab80787f9-5573052-images-thumbs&n=13',
            'price': 2100.00,
            'duration': 10,
            'popularity': 88,
            'tags': ['семейный', 'развлечения', 'пляж', 'парки аттракционов', 'отдых'],
            'destination_type': 'fl',
        },
        {
            'name': _('Калифорния: Сан-Франциско и Лос-Анджелес'),
            'description': _('10 дней по Золотому штату: мост Золотые Ворота, Голливуд, Беверли-Хиллз, Силиконовая долина и винодельни Напа'),
            'image_url': 'https://avatars.mds.yandex.net/i?id=850f41908ccdb1920b5d08c7bc7489a7edb67593-5245909-images-thumbs&n=13',
            'price': 1950.50,
            'duration': 10,
            'popularity': 90,
            'tags': ['город', 'вино', 'пляж', 'технологии', 'кино'],
            'destination_type': 'west',
        },
        {
            'name': _('Аляска: Северное сияние'),
            'description': _('Уникальный тур за полярный круг: наблюдение за северным сиянием, ледники, киты и культура инуитов'),
            'image_url': 'https://avatars.mds.yandex.net/i?id=1e59a4b208875d2db7dc34a02a5b6d77_l-5875509-images-thumbs&n=13',
            'price': 3200.00,
            'duration': 8,
            'popularity': 78,
            'tags': ['природа', 'экзотика', 'приключения', 'фотографии', 'уникальное'],
            'destination_type': 'custom',
        },
        {
            'name': _('Техас: Ковбои и космос'),
            'description': _('Автопутешествие по Техасу: ранчо ковбоев, космический центр NASA в Хьюстоне, Остин - музыкальная столица'),
            'image_url': 'https://i.pinimg.com/originals/5a/24/89/5a2489608ab645dce30c48f6076b7b6f.jpg',
            'price': 1650.00,
            'duration': 9,
            'popularity': 75,
            'tags': ['ковбои', 'космос', 'музыка', 'автопутешествие', 'история'],
            'destination_type': 'west',
        },
    ]

    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            request.session['booking_data'] = form.cleaned_data
            return redirect('success_page')

    return render(request, 'tours/index.html', {
        'destinations': destinations,
        'form': form,
    })

def success_page(request):
    data = request.session.get('booking_data', {})
    return render(request, 'tours/success.html', {'data': data})