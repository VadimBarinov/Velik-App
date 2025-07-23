from catalog.utils import menu
from velik import settings


def get_catalog_context(request):
    return {
        'main_menu': menu,
        'default_img': settings.DEFAULT_BIKE_IMAGE,
        'default_profile': settings.DEFAULT_PROFILE_IMAGE
    }
