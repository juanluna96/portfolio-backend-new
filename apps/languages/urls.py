# urls.py
from django.urls import path
from apps.languages.views import LanguageListView

urlpatterns = [
    path('languages/', LanguageListView.as_view(), name='language-list'),
]
