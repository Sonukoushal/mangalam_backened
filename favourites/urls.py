from django.urls import path 
from .views import FavouriteView

urlpatterns = [
    path("favourites/",FavouriteView.as_view(),name='favourite'),
]
