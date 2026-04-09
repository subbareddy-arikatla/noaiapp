from django.urls import path
from .views import student_details,book_details,book_list,student_list,QuestionDetails,QuestionList,productdemoList,CustomerDetails,Customerlist,bulkStudentCreate
from . import views

urlpatterns=[
    path('books/',views.book_list,name='books-list'),
    path('books/{id}/',views.book_details,name='books-list'),
    path('students/',views.student_list,name='student-list'),
    path('students/<int:pk>/',views.student_details,name='student-list'),
    path('blukstudents/',views.bulkStudentCreate, name='bulk student create'),
    path('question/',views.QuestionList,name='question list'),
    path('question/<int:pk>/',views.QuestionDetails,name='question details'),
    path('products/', views.get_products),
    path('create/', views.create_product),
    path('crash/', views.crash_api),
    path('update/<int:id>/', views.update_product),
    path('productsdemo/',views.productdemoList,name='productdemolist'),
    path('productsdemo/<int:id>/',views.productdemoDetails,name='productdemodetails'),
    path('customer/',views.Customerlist,name='customerlist'),
    path('customer/<int:pk>/',views.CustomerDetails,name='customerlist')
]