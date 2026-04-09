from django.urls import path
from .views import student_details,student_list,BookListCreateView,BookDetailView,QuestionDetails,QuestionList,productdemoList,CustomerDetails,Customerlist,bulkStudentCreate
from . import views

urlpatterns=[
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]