import debug_toolbar
from django.urls import re_path
from django.contrib import admin
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from myapp.views import (SchoolView, CollegeView, UniverstyView, UserViewSet, UserView, NestedData,
                         AffiliationView, GetDataS, GetDataH,  GetDataHI, GetDataSlug, GetDataP,
                         IndustriesView, UniverstyNestedView, DepartmentView, FeeView, DepartmentNestedView)
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf import settings
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="My Personal Project",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


router = DefaultRouter()
router.register(r'school', SchoolView, basename='school')
router.register(r'college', CollegeView, basename='college')
router.register(r'universty', UniverstyView, basename='universty')
router.register(r'user', UserViewSet, basename='user')
router.register(r'getdata-N', NestedData, basename='nested_data')
router.register(r'getdata-S', GetDataS, basename='string_related')
router.register(r'getdata-H', GetDataH, basename='hyperlinked_data')
router.register(r'getdata-HI', GetDataHI, basename='hyperlinked_identity')
router.register(r'getdata-slug', GetDataSlug, basename='slug_data')
router.register(r'getdata-P', GetDataP, basename='primary_key_data')
router.register(r'affiliate', AffiliationView, basename='affiliation')
router.register(r'industry', IndustriesView, basename='industry')
router.register(r'universty-nested', UniverstyNestedView, basename='universty_nested')
router.register(r'department', DepartmentView, basename='department')
router.register(r'fee', FeeView, basename='fee')
router.register(r'departpartment-nested', DepartmentNestedView, basename='department-nested')
router.register(r'user-c', UserView, basename='user-c')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('myapp.urls')),
    path('', include(router.urls)),
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify_token/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(debug_toolbar.urls)),
    re_path(r'^auth/', include('rest_framework_social_oauth2.urls', namespace="drf")),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
              ] + router.urls


urlpatterns += static(settings.MEDIA_URL, document_root='settings.MEDIA_ROOT')


