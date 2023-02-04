from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('<int:product_id>/detail/', views.product_detail, name='product_detail'),
    path('<int:product_id>/detail/comment/new', views.new_comment, name='create_comment'),
    path('<int:product_id>/detail/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
]
