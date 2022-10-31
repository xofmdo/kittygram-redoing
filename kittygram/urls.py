from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path

from cats.views import CatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')

urlpatterns = [
    path('', include(router.urls), name='api-root'),
    path('admin/', admin.site.urls),
]
