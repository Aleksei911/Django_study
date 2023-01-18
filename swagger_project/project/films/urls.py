from django.urls import include, path
from rest_framework import routers
from .views import FilmsViewSet, ActorViewSet, GenreViewSet

router = routers.DefaultRouter()

router.register(r'Films', FilmsViewSet)
router.register(r'Actors', ActorViewSet)
router.register(r'Genre', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
