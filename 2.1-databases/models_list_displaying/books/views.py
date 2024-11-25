from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {"books_list": books}
    return render(request, template, context)


def books_pub_date_view(request, pub_date):
    template = 'books/books_pagi.html'
    books_pub_date = Book.objects.filter(pub_date=pub_date)
    books_next = (Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first())
    if books_next:
        books_next = str(books_next.pub_date)
    else:
        books_next = "Дальше нет дат"
    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()
    if books_previous:
        books_previous = str(books_previous.pub_date)
    else:
        books_previous = "Дальше нет дат"
    context = {"books_list": books_pub_date,
               "books_next": books_next,
               "books_previous": books_previous,
               }
    return render(request, template, context)