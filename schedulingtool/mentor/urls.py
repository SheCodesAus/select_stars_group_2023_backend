from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('event/', views.EventListView.as_view()),
    path('event/<int:pk>/', views.EventDetailView.as_view()),
    path('onboarding/', views.OnboardingListView.as_view()),
    path('onboarding/<int:pk>/', views.OnboardingDetailView.as_view()),
    path('mentor/', views.MentorListView.as_view()),
    path('mentor/<int:pk>/', views.MentorDetailView.as_view()),
    path('tech_stack/', views.Tech_StackListView.as_view()),
    path('tech_stack/<int:pk>/', views.Tech_StackDetailView.as_view()),

    
]

urlpatterns = format_suffix_patterns(urlpatterns)