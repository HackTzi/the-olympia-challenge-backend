"""techstore URL Configuration"""

# Django
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

# Django REST Framework & YASG
from rest_framework import routers, permissions
from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Views
from products import views as products_views
from customers import views as customers_views

schema_view = get_schema_view(
    openapi.Info(
        title="ConnectCare API",
        default_version='v2',
        description="The API for ConnectCareHero",
        contact=openapi.Contact(email="developer@nexgen-solutions.local"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = routers.DefaultRouter()
router.register(r'categories', products_views.CategoryViewSet)
router.register(r'products', products_views.ProductViewSet)
router.register(r'customers', customers_views.CustomerViewSet)

urlpatterns = [
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('coupon/<int:pk>/check/', products_views.CouponCheckView.as_view(), name='coupon_check'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
