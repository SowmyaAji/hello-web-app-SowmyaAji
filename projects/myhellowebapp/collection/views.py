from django.shortcuts import render, redirect
from collection.forms import BookForm

from collection.models import Book


from django.conf import settings
from django.conf.urls.static import static
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):

    books = Book.objects.all()

    # # books = Book.objects.filter(name='Top favorite book').order_by('name')
    # books = Book.objects.all().order_by('?')

    return render(request, 'index.html', {

        'books': books,
    })


def book_detail(request, slug):

    book = Book.objects.get(slug=slug)

    return render(request, 'books/book_detail.html', {
        'book': book,
    })


@login_required
def edit_book(request, slug):
    # grab the object...

    book = Book.objects.get(slug=slug)
# set the form we're using...
    # if we're coming to this view from a submitted form,

    if book.user != request.user:
        raise Http404

    if request.method == 'POST':

        # grab the data from the submitted form
        form = BookForm(data=request.POST, files=request.FILES, instance=book)

        if form.is_valid():
            # save the new data
            form.save()

            return redirect('book_detail', slug=book.slug)

    else:
        form = BookForm(instance=book)

    return render(request, 'books/edit_book.html', {
        'book': book,
        'form': form,
    })


def create_book(request):
    form_class = BookForm
    # book = Book.objects.get(slug=slug)
    if request.method == 'POST':

        form = form_class(data=request.POST, files=request.FILES)

        if form.is_valid():

            book = form.save(commit=False)
            book.user = request.user
            book.slug = slugify(book.name)

            book.save()

            return redirect('book_detail', slug=book.slug)

    else:
        form = form_class()

    return render(request, 'books/create_book.html', {
        # 'book': book,
        'form': form,
    })
