from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('books/', BookListCreateView.as_view()),
    path('books/<int:id>', BookDetailView.as_view()),
]
