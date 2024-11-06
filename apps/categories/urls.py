from django.urls import path
from apps.categories.views import CategoryListByLanguage

urlpatterns = [
    path('categories', CategoryListByLanguage.as_view(), name='category-list-by-language'),
]
