import random
from django import template
from catalog.models import BikeModel, BikeCharacteristicValue
from velik import settings


# регистрация новых тегов
register = template.Library()


@register.filter
def find_image(image_url):
    try:
        if (image_url and image_url.file):
            return True
    except FileNotFoundError:
        return False


@register.inclusion_tag('catalog/carousel.html')
def show_carousel():
    bikes = BikeModel.objects.order_by('?')[:3]
    bikes_characteristics = {}

    for item in bikes:
        bikes_characteristics[item.slug] = BikeCharacteristicValue.get_bike_characteristics(item)

    return {
        'bikes': bikes,
        'bikes_characteristics': bikes_characteristics,
        'default_img': settings.DEFAULT_BIKE_IMAGE,
        }


@register.simple_tag
def get_random_characteristics(bikes, bike_slug):
    dict_data = bikes.get(bike_slug)
    random_values = random.choice(list(dict_data))
    while len(dict_data.get(random_values)) < 5 and len(dict_data) > 1:
        del dict_data[random_values]
        random_values = random.choice(list(dict_data))
    result = list(dict_data.get(random_values).items())
    if len(result) > 5:
        result = result[:5]
    return result


@register.simple_tag
def my_range(first, second):
    return list(range(first, second))


@register.filter
def get_value_from_dict(dict_data, key):
    return dict_data.get(key)
