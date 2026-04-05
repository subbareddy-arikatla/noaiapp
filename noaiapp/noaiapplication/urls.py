from django.urls import path
from .views import student_details,student_list,QuestionDetails,QuestionList

urlpatterns=[
    path('students/',student_list.as_view(),name='student-list'),
    path('students/<int:pk>/',student_details.as_view(),name='student-list'),
    path('question/',QuestionList.as_view(),name='question list'),
    path('question/<int:pk>/',QuestionDetails.as_view(),name='question details'),
]