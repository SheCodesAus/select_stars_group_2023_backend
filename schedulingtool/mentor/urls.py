from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('event/', views.EventList.as_view()),
    path('event/<int:pk>/', views.EventDetail.as_view()),
    path('mentor/', views.MentorList.as_view()),
    path('mentor/<int:pk>/', views.MentorDetail.as_view()),
    path('tech_stack/', views.Tech_StackList.as_view()),
    path('tech_stack/<int:pk>/', views.Tech_StackDetail.as_view()),

    
]

urlpatterns = format_suffix_patterns(urlpatterns)