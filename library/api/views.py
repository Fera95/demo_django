from django.shortcuts import render  # noqa: F401
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


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


class BookDetailView(APIView):

    def get_object(self,id):

        try:

            return Book.objects.get(id=id)

        except Book.DoesNotExist:

            return None


    def get(self,request,id):

        book = self.get_object(id)

        if not book:

            return Response(

            {

                "status":"error" ,"data":"Not Found"

            },

            status=status.HTTP_404_NOT_FOUND
            )
        

        serializer = BookSerializer(book)

        return Response(

            {

                "status": "success" , "data": serializer.data

            },

            status=status.HTTP_200_OK
        )
    def jls_extract_def(self, serializer):
        return Response({"status":"error","data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        book = self.get_object(id)
        if not book:
            return Response(
            {
                "status":"error" ,"data":"Not Found"
            },
            status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "status": "success" , "data": serializer.data
            },
            status=status.HTTP_200_OK
            )
        return self.jls_extract_def(serializer)

    def delete(self,request,id):
        book = self.get_object(id)

        if not book:

            return Response(

            {

                "status":"error" ,"data":"Not Found"

            },

            status=status.HTTP_404_NOT_FOUND
            )

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)