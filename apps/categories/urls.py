from django.urls import path
from apps.categories.views import CategoryListByLanguage, CategoriesDescriptionWithAllLanguages

urlpatterns = [
    path('categories', CategoryListByLanguage.as_view(), name='category-list-by-language'),
    path('categories/description', CategoriesDescriptionWithAllLanguages.as_view(), name='categories-description-with-all-languages'),  # Nueva ruta para la lista de categorías
]
