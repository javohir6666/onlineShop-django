from django.urls import path
from main.views import IndexView,CategoryView, ClotheCategoryView
app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path(f'<str:category_name>/category/', CategoryView.as_view(), name='category'),
    path(f'<str:clotheCategory_title>/category/clothes/', ClotheCategoryView.as_view(), name='clotheCategory'),
]
