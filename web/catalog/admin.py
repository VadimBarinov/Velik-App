from django.contrib import admin
from .models import BikeModel, BikeMark, BikeModification, BikeCharacteristic, BikeCharacteristicValue, BikeStars, BikeFavourites


@admin.register(BikeModel)
class BikeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'slug', 'img_url')


@admin.register(BikeMark)
class BikeMarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(BikeModification)
class BikeModificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'bike_model', 'name')


@admin.register(BikeCharacteristic)
class BikeCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_parent')


@admin.register(BikeCharacteristicValue)
class BikeCharacteristicValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'bike_characteristic', 'bike_modification')


@admin.register(BikeStars)
class BikeStarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bike', 'star')


@admin.register(BikeFavourites)
class BikeFavouritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bike')
