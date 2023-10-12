from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.all()
    
def book_list(request):
    return BookListView.as_view()(request)

class BookDetailView(LoginRequiredMixin, generic.DetailView):
	model = Book

def book_detail(request, pk):
	return BookDetailView.as_view()(request, pk)
