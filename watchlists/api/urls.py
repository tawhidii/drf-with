
from django.urls import path
# from watchlists.api.views import movies,movie_details
from watchlists.api.views import MovieList,MovieDetailsView
urlpatterns = [

    path('list',MovieList.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetailsView.as_view(),name='movie-detail')
]
