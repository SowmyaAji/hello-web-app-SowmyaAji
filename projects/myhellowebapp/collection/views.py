from django.shortcuts import render, redirect
from collection.forms import BookForm
# from collection.forms import ThingForm
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


def edit_book(request, slug):
    # grab the object...
    book = Book.objects.get(slug=slug)
# set the form we're using...
    form_class = BookForm
    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=book)

        if form.is_valid():
            # save the new data
            form.save()
            return redirect('book_detail', slug=book.slug)

    else:
        form = form_class(instance=book)

    return render(request, 'books/edit_book.html', {
        'book': book,
        'form': form,
    })
