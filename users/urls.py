from django.urls import path
from .views import UserCreateView, UserDetailView, UserListView, UserDeleteView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('profile/', UserDetailView.as_view(), name='user-profile'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete-by-id'),
    path('delete/', UserDeleteView.as_view(), name='user-delete'),
    path('users/', UserListView.as_view(), name='user-list'),
]
