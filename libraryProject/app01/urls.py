from django.urls import path
from app01 import views
urlpatterns = [
    path("", views.index),
    path("add_publisher/", views.add_publisher),
    path("publisher_list/", views.publisher_list),
    path("edit_publisher/", views.edit_publisher),
    path("delete_publisher/", views.delete_publisher),
    path("book_list/", views.book_list),
    path("add_book/", views.add_book),
    path("delete_book/", views.delete_book),
    path("edit_book/", views.edit_book),
    path("user_register/", views.register),
    path("borrow_list/", views.borrow_list),
    path("borrow_book/", views.borrow_book),
    path("my_books/", views.my_books),
    path("return_book/", views.return_book),
]