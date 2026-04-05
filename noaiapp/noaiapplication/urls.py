from django.urls import path
from .views import student_details,student_list,QuestionDetails,QuestionList
from . import views

urlpatterns=[
    path('students/',views.student_list,name='student-list'),
    path('students/<int:pk>/',views.student_details,name='student-list'),
    path('question/',views.QuestionList,name='question list'),
    path('question/<int:pk>/',views.QuestionDetails,name='question details'),
    path('products/', views.get_products),
    path('create/', views.create_product),
    path('crash/', views.crash_api),
    path('update/<int:id>/', views.update_product),
]