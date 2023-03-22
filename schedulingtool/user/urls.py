from django.urls import path
from . import views

urlpatterns = [
    path('create-account/', views.CreateCustomUser.as_view(), name = 'create-customuser'),
    path('user/', views.CustomUserList.as_view(), name = 'customuser-list'),
    path('user/<int:pk>/', views.CustomUserDetail.as_view(), name = 'customuser-detail'),
]