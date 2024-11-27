from django.urls import path
from .views import (
    HomePageAPIView,
    TeacherPageAPIView,
    BlogPageAPIView,
    BlogDetailAPIView,
)

urlpatterns = [
    path('homepage/', HomePageAPIView.as_view(), name='home-page-list'),
    path('teacherpage/',TeacherPageAPIView.as_view(),name='teacher-page-view'),
    path('blogpage/',BlogPageAPIView.as_view(),name='blog-page-list'),
    path('blog/<slug:slug>/', BlogDetailAPIView.as_view(), name='blog-detail'),
]