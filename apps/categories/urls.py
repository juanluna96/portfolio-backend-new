from django.urls import path
from apps.categories.views import CategoryListByLanguage, CategoriesDescriptionWithAllLanguages, CategoryProjectsView

urlpatterns = [
    path('categories', CategoryListByLanguage.as_view(), name='category-list-by-language'),
    path('categories/description', CategoriesDescriptionWithAllLanguages.as_view(), name='categories-description-with-all-languages'),  
    path('category/projects', CategoryProjectsView.as_view(), name='category-projects'),
]
