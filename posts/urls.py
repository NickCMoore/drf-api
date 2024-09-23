from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),  # Replace with your actual view name
    path('<int:pk>/', views.PostDetail.as_view(), name='post-detail'),  # Replace with your actual view name
]
