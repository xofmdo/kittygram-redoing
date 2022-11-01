from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import include, path

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls), name='api-root'),
    path('admin/', admin.site.urls),
]
