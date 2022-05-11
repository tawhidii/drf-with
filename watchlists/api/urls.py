
from django.urls import path
# from watchlists.api.views import movies,movie_details
from watchlists.api.views import (
    WatchListView,
    WatchListDetailsView,
    StreamingPlatformListView,
    StreamingPlatformDetailsView
)
urlpatterns = [

    path('list',WatchListView.as_view(),name='movie-list'),
    path('<int:pk>',WatchListDetailsView.as_view(),name='movie-detail'),
    path('stream',StreamingPlatformListView.as_view(),name='stream'),
    path('stream/<int:pk>/',StreamingPlatformDetailsView.as_view(),name='stream-details')
]
