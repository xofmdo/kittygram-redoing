from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet, basename='cats')

urlpatterns = [
    path('', include(router.urls)),
]
