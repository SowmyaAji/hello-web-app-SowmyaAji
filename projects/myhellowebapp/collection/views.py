from django.shortcuts import render
from collection.models import Book
# Create your views here.
# Create your views here.


def index(request):
    # this is your new view
    books = Book.objects.all()

    # # books = Book.objects.filter(name='Top favorite book').order_by('name')
    # books = Book.objects.all().order_by('?')

    return render(request, 'index.html', {

        'books': books,
    })


def book_detail(request, slug):

    # grab the object...
    book = Book.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'books/book_detail.html', {
        'book': book,
    })
