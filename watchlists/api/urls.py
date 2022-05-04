
from django.urls import path
from watchlists.api.views import movies,movie_details
urlpatterns = [

    path('list',movies,name='movie-list'),
    path('<int:pk>',movie_details,name='movie-detail')
]
