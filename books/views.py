from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Books


class BookListView(generic.ListView):
    model = Books
    template_name = 'books/book_list.html'
    context_object_name = 'book'
    
    def get_queryset(self):
        return Books.objects.all().order_by('-id')
    

class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Books
    fields =[
        'title',
        'author',
        'description',
        'price',
    ]
    template_name = 'books/book_create.html'
    context_object_name = 'form'
    

class BookUpdateView(generic.UpdateView):
    model = Books
    fields =[
        'title',
        'author',
        'description',
    ]
    template_name='books/book_update.html'
    context_object_name = 'form'    
    context_object_name = 'book'    


class BookDleteView(generic.DeleteView):
    model = Books
    template_name='books/book_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')
































