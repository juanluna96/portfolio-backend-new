from django.urls import path
from .views import AreaWithCategoriesProjectsView

urlpatterns = [
    path('areas-categories/', AreaWithCategoriesProjectsView.as_view(), name='areas-categories-projects'),
]
