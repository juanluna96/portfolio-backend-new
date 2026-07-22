from django.urls import path
from .views import LastBiographyView

urlpatterns = [
    path('last-biography/', LastBiographyView.as_view(), name='last-biography'),
]
