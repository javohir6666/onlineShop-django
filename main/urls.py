from django.urls import path
from main.views import IndexView,CategoryView
app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path(f'<str:category_name>/category/', CategoryView.as_view(), name='category'),
]
