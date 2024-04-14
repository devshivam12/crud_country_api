from django.contrib import admin
from django.urls import path, include
from api.views import CountryViewSet
from rest_framework import routers
from .views import CountryCreateAPIView,CountryUpdateAPIView

router= routers.DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('cc/', CountryCreateAPIView.as_view(), name='country-create'),
    path('up/<int:country_id>/', CountryUpdateAPIView.as_view(), name='update-country')
]
# urls.py
