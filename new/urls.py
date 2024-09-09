from django.urls import include, path
from rest_framework.routers import DefaultRouter
from new.views import KollaView

router = DefaultRouter()

router.register("kolla", KollaView, basename="kolla")

urlpatterns = [
    path('', include(router.urls))
]
