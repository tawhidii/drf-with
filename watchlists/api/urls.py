
from django import views
from django.urls import path,include
# from watchlists.api.views import movies,movie_details
from rest_framework.routers import DefaultRouter
from watchlists.api.views import (
    WatchListView,
    WatchListDetailsView,
    # StreamingPlatformListView,
    # StreamingPlatformDetailsView,
    ReviewListView,
    ReviewDetailsView,
    ReviewCreateView,
    SteamingPlatformView
)

router = DefaultRouter()
router.register('stream',SteamingPlatformView,basename='streamplatform')

urlpatterns = [

    path('list',WatchListView.as_view(),name='movie-list'),
    path('<int:pk>',WatchListDetailsView.as_view(),name='movie-detail'),
    path('',include(router.urls)),

    # path('stream',StreamingPlatformListView.as_view(),name='stream'),
    # path('stream/<int:pk>',StreamingPlatformDetailsView.as_view(),name='stream-details'),

    # review urls 
    path('<int:pk>/reviews',ReviewListView.as_view(),name='review-list'),
    path('reviews/<int:pk>',ReviewDetailsView.as_view(),name='review-details'),
    path('<int:pk>/review-create',ReviewCreateView.as_view(),name='review-create')
]
