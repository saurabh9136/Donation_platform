from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'ngos', views.NGOViewSet)
router.register(r'donations', views.DonationViewSet)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', views.login, name='login'),
]
