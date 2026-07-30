from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListCreateView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response({"status":"sucess", "data":serializer.data}, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status":"sucess","data":serializer.data},
                status=status.HTTP_201_CREATED
            )
        #Si no es valido
        return Response({"status":"error","data": serializer.errors},status=status.HTTP_400_BAD_REQUEST)