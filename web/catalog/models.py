from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import F
import pandas as pd


class BikeMark(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class BikeModel(models.Model):
    mark = models.ForeignKey(
        'BikeMark', on_delete=models.PROTECT, related_name='mark'
        )
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    img_url = models.ImageField(
        upload_to="bikes/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True
        )
    star = models.FloatField(default=0)
    star_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bike', kwargs={'bike_slug': self.slug})

    @staticmethod
    def sort_by_fav_or_stars(set_bikes, set_fav_or_stars):
        return sorted(
            set_bikes,
            key=lambda x: set_fav_or_stars.get(bike=x).pk,
            reverse=True
        )


class BikeModification(models.Model):
    bike_model = models.OneToOneField(
        'BikeModel', on_delete=models.PROTECT, related_name='bike_model'
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BikeCharacteristic(models.Model):
    name = models.CharField(max_length=255)
    id_parent = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class BikeCharacteristicValue(models.Model):
    value = models.CharField(max_length=255)
    bike_characteristic = models.ForeignKey(
        'BikeCharacteristic',
        on_delete=models.PROTECT,
        related_name='bike_characteristic'
    )
    bike_modification = models.ForeignKey(
        'BikeModification',
        on_delete=models.PROTECT,
        related_name='bike_modification'
    )

    def __str__(self):
        return str(self.pk)

    @staticmethod
    def get_bike_characteristics(bike):
        id_parents = BikeCharacteristic.objects.filter(id_parent=None)
        bike_characteristics = {}
        characteristics_value = bike.bike_model.bike_modification.all()

        for char in characteristics_value:
            if bike_characteristics.get(id_parents.get(pk=char.bike_characteristic.id_parent).name):
                temp = bike_characteristics[id_parents.get(pk=char.bike_characteristic.id_parent).name]
                temp[char.bike_characteristic.name] = char.value
                bike_characteristics[id_parents.get(pk=char.bike_characteristic.id_parent).name] = temp
            else:
                bike_characteristics[id_parents.get(pk=char.bike_characteristic.id_parent).name] = {
                    char.bike_characteristic.name: char.value
                    }
        return bike_characteristics


class BikeFavourites(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='user_favorite'
    )
    bike = models.ForeignKey(
        'BikeModel',
        on_delete=models.PROTECT,
        related_name='bike_favorite'
    )


class PageQuerySet(models.QuerySet):
    def delete(self):
        return super().delete()


class PageManager(models.Manager):
    def get_queryset(self):
        return PageQuerySet(model=self.model, using=self._db, hints=self._hints)


class BikeStars(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='user_star'
    )
    bike = models.ForeignKey(
        'BikeModel',
        on_delete=models.PROTECT,
        related_name='bike_star'
    )
    star = models.FloatField()

    objects = PageManager()

    def save(self, *args, **kwargs):
        BikeModel.objects.filter(pk=self.bike.pk).update(
            star=(F('star_count')*F('star')+self.star)/(F('star_count')+1),
            star_count=F('star_count')+1,
        )
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        current_bike = BikeModel.objects.filter(pk=self.bike.pk)
        if current_bike.get().star_count < 2:
            current_bike.update(
                star=0,
                star_count=0,
            )
        else:
            current_bike.update(
                star=(F('star_count')*F('star')-self.star)/(F('star_count')-1),
                star_count=F('star_count')-1,
            )
        super().delete(*args, **kwargs)
