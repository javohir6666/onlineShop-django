from django.urls import path
from users import views
from .views import ProfileView,UpdateProfileView
app_name = 'users'
urlpatterns = [
    path('login/add_user_save/', views.add_user_save),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', UpdateProfileView.as_view(), name='updateProfile'),
]
