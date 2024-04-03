from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Movie
from .serializers import MovieSerializer
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    parser_classes = (MultiPartParser, FormParser)


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
