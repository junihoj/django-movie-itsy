from django.urls import path
# from .views import MovieListCreateAPIView
from . import views
from rest_framework import routers

app_name = 'movie'

router = routers.DefaultRouter()
router.register('movie', views.MovieViewSet)
urlpatterns = [
    # path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    # other URL patterns if needed
]
