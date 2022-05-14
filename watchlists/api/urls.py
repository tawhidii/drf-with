
from django import views
from django.urls import path
# from watchlists.api.views import movies,movie_details
from watchlists.api.views import (
    WatchListView,
    WatchListDetailsView,
    StreamingPlatformListView,
    StreamingPlatformDetailsView,
    ReviewListView,
    ReviewDetailsView,
    ReviewCreateView
)
urlpatterns = [

    path('list',WatchListView.as_view(),name='movie-list'),
    path('<int:pk>',WatchListDetailsView.as_view(),name='movie-detail'),
    path('stream',StreamingPlatformListView.as_view(),name='stream'),
    path('stream/<int:pk>',StreamingPlatformDetailsView.as_view(),name='stream-details'),

    # review urls 
    path('stream/<int:pk>/reviews',ReviewListView.as_view(),name='review-list'),
    path('stream/reviews/<int:pk>',ReviewDetailsView.as_view(),name='review-details'),
    path('stream/<int:pk>/review-create',ReviewCreateView.as_view(),name='review-create')
]
