
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlists.models import Movies
from watchlists.api.serializers import MovieSerializer

from rest_framework.views import APIView


# CLASS BASED VIEW #
class MovieList(APIView):
    def get(self,request):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MovieDetailsView(APIView):
    def get(self,request,pk):
        try:
            movie = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response({'error': f'{pk} not found !!'},status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    
    def put(self,request,pk):
        movie = Movies.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
        movie = Movies.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






































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


