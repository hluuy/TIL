from django.shortcuts import render, redirect
from libraries.models import Book, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {
    'books': books,
    }
    return render(request, 'libraries/book_list.html', context)

def book_detail(request, book_pk):    
    book = Book.objects.get(pk=book_pk)    
    review_form = ReviewForm()
    reviews = book.review_set.all()
    context = {
        'book': book,
        'pk': book.pk,
        'title': book.title,
        'description': book.description,
        'review_form' : review_form,
        'reviews' : reviews,
    }
    return render(request, 'libraries/book_detail.html', context)


def review_create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review_form.save()
        return redirect('libraries:book_detail', book.pk)
    
    review_form = ReviewForm()
    
    context = {
        'book' : book,
        'review_form' : review_form,
    }
    return render(request, 'libraries/book_detail.html', context)


def review_delete(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('libraries:book_detail', book_pk)