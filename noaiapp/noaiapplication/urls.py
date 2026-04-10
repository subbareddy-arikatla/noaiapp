from django.urls import path
from .views import student_details,student_list,book_list_create,book_detail,QuestionDetails,QuestionList,productdemoList,CustomerDetails,Customerlist,bulkStudentCreate
from . import views

urlpatterns=[
     path('books/', book_list_create, name='book_list_create'),
    path('books/<int:id>/', book_detail, name='book_detail'),
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