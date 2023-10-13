from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        # form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = Comment.objects.all()
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            # form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/create.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')

def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment_form.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie' : movie,
        'comment_form' : comment_form,
    }
    return render(request, 'movies/detail.html', context)

def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)