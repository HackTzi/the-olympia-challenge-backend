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
        title="Jipeek API",
        default_version='v1',
        description="The API for Jippek Store",
        contact=openapi.Contact(email="jipeek@mail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = routers.DefaultRouter()
router.register(r'categories', products_views.CategoryViewSet)
router.register(r'products', products_views.ProductViewSet)
router.register(r'customers', customers_views.CustomerViewSet)
router.register(r'users', customers_views.UserViewSet)
router.register(r'collections', products_views.CollectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('coupon/<int:pk>/check/', products_views.CouponCheckView.as_view(), name='coupon_check'),
    path('currencies/', customers_views.CurrencyListView.as_view(), name='currency_list'),
    path('countries/', customers_views.CountryListView.as_view(), name='countries_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
