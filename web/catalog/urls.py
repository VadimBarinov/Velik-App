from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path("catalog/", views.ShowCatalog.as_view(), name='catalog'),
    path("favourites/", views.ShowFavourites.as_view(), name='favourites'),
    path("about/", views.ShowAbout.as_view(), name='about'),
    path("bike/<slug:bike_slug>/", views.ShowBike.as_view(), name="bike"),
    path("stars/", views.ShowStars.as_view(), name='stars'),
]
