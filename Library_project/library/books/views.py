from django.shortcuts import render
from .models import Book, Comment
from .form import CommentForm


# Create your views here.
def book_index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/books_index.html', context)


def book_author(request, author):
    books = Book.objects.filter(
        author__name__contains=author
    )
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'books/book_author.html', context)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                comment_author=form.cleaned_data['comment_author'],
                body=form.cleaned_data['body'],
                book=book,
            )
            comment.save()

    comments = Comment.objects.filter(book=book)
    context = {
        'book': book,
        'comments': comments,
        'form': form,
    }
    return render(request, 'books/books_detail.html', context)
