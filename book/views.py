from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
# Create your views here.

def homepage(request):
    books=Book.objects.all()
    return render(request,'book_list.html',{'books':books})


def add_book(request):

    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm()

        context = {
            "form": book_form,
        }
        return render(request, "book.html", context)

def update_book(request,id):
    specific_book = Book.objects.get(id=id)

    if request.method == "POST":
        book_form = BookForm(request.POST, instance=specific_book)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
     
        book_form = BookForm(instance=specific_book)
        context = {
            "form": book_form,
        }
        return render(request, "book.html", context)
    

def display_book(request,id):
    specific_book = Book.objects.get(id=id)
   
    context = {
        "book": specific_book,
    }
    return render(request, "display_book.html", context)

def delete_book(request,id):
    book = Book.objects.get(id=id)
   # return book
    book.delete()
    return redirect("book_list")