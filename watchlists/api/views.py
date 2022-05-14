
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlists.models import WatchList,StreamingPlatform,Review
from watchlists.api.serializers import(
    WatchListSerializer,
    StreamingPlatformSerializer,
    ReviewSerializer
    )
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class StreamingPlatformListView(APIView):
    def get(self,request):
        streams = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(streams,many=True,context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully created !!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class StreamingPlatformDetailsView(APIView):

    def get(self,request,pk):
        try:
            stream = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': f'{pk} not found !!'},status=status.HTTP_404_NOT_FOUND)
        serializer = StreamingPlatformSerializer(stream,context={'request': request})
        return Response(serializer.data)
    
    def put(self,request,pk):
        stream = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(stream,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class WatchListView(APIView):
    def get(self,request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message' : 'Created Successfully !!',
                'data': serializer.data
            }
            return Response(response)
        else:
            return Response(serializer.errors)

   


class WatchListDetailsView(APIView):
    def get(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': f'{pk} not found !!'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)

        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
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
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(watchlist=self.kwargs['pk'])


class ReviewDetailsView(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        serializer.save(watchlist=watchlist)


































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


