from django.urls import path
from .views import student_details,student_list

urlpatterns=[
    path('students/',student_list.as_view(),name='student-list'),
    path('students/<int:pk>/',student_details.as_view(),name='student-list')
]