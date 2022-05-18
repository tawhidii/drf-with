from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlists.models import WatchList, StreamingPlatform, Review
from watchlists.api.serializers import (
    WatchListSerializer,
    StreamingPlatformSerializer,
    ReviewSerializer
)
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from watchlists.api.permissions import ReviewIsUserOrReadOnly


# Example of viewset
class SteamingPlatformView(viewsets.ModelViewSet):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer

    # For ViewSet only 
    # def list(self, request):
    #     queryset = StreamingPlatform.objects.all()
    #     serializer = StreamingPlatformSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = StreamingPlatform.objects.all()
    #     platform = get_object_or_404(queryset, pk=pk)
    #     serializer = StreamingPlatformSerializer(platform)
    #     return Response(serializer.data)


# class StreamingPlatformListView(APIView):
#     def get(self,request):
#         streams = StreamingPlatform.objects.all()
#         serializer = StreamingPlatformSerializer(streams,many=True,context={'request': request})
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = StreamingPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Successfully created !!'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

# class StreamingPlatformDetailsView(APIView):

#     def get(self,request,pk):
#         try:
#             stream = StreamingPlatform.objects.get(pk=pk)
#         except StreamingPlatform.DoesNotExist:
#             return Response({'error': f'{pk} not found !!'},status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamingPlatformSerializer(stream,context={'request': request})
#         return Response(serializer.data)

#     def put(self,request,pk):
#         stream = StreamingPlatform.objects.get(pk=pk)
#         serializer = StreamingPlatformSerializer(stream,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class WatchListView(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Created Successfully !!',
                'data': serializer.data
            }
            return Response(response)
        else:
            return Response(serializer.errors)


class WatchListDetailsView(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': f'{pk} not found !!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)

        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Code with generic view
# class ReviewListView(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# concrete view 
class ReviewListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(watchlist=self.kwargs['pk'])


class ReviewDetailsView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data.get('rating'))
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError({'message': 'You already posted review for this !!'})

        if watchlist.avg_rating == 0:
            watchlist.avg_rating = serializer.validated_data.get('rating')
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2
        watchlist.total_rating += 1
        watchlist.save()
        serializer.save(watchlist=watchlist, review_user=review_user)

#### FUNCTION BASED VIEW ###

# @api_view(['GET','POST'])
# def movies(request):
#     if request.method == 'GET':
#         movies = Movies.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         print(request.data)
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie = Movies.objects.get(pk=pk)
#         except Movies.DoesNotExist:
#             return Response({'error':'Object not found!!'},status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movies.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

#     if request.method == 'DELETE':
#         movie = Movies.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
