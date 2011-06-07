from dtl.models import Book, BookOnLoan, Author, Category, BookCopy
from django.db.models import Q
from django import forms
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


def list_books(request):
    '''Renders a paginated list of books.
    '''
    b = paginate(Book.objects.all(), 15, request)

    return render_to_response('list.html', {'books': b})


def book_detail(request, book_id):
    '''Renders a page that shows detailed info for a single book.
    '''
    b = get_object_or_404(Book, pk=book_id)
    c = BookCopy.objects.filter(book=book_id)
    l = [is_loaned(bcid.id) for bcid in c]
    c = zip(c, l)
    return render_to_response('detail.html', {'book': b, 'copies': c})


def author_detail(request, author_id):
    '''Renders a page that shows detailed info for a single author.
    '''
    a = get_object_or_404(Author, pk=author_id)
    return render_to_response('author_detail.html', {'author': a})


def category_detail(request, category_id):
    '''Renders a page that shows detailed info for a category.
    '''
    c = get_object_or_404(Category, pk=category_id)
    return render_to_response('category_detail.html', {'category': c})


def search(request):
    '''Renders a search page.
    '''
    q = request.GET.get('q', '')
    if q:
        b = process_query(q, Book)
        b = paginate(b, 15, request)
        return render_to_response('list.html', {'books': b})
    else:
        results = []
    return render_to_response("search.html", {
        "results": results,
        "query": q
    })


def login(request):
    return render_to_response("login.html")


# Administration dashboard views
@login_required()
def dashboard(request):
    return render_to_response("dashboard.html")


# Helper functions
def is_loaned(bid):
    '''For a given book_id, checks if a book is loaned.

    Returns bool.'''
    l = BookOnLoan.objects.filter(book__id=bid, date_returned__isnull=True)
    return bool(l)


def paginate(o, n, request):
    '''Paginates a list of objects and number of elements per page.

    Returns a paginator object.'''
    paginator = Paginator(o, n)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        return paginator.page(page)
    except (EmptyPage, InvalidPage):
        return paginator.page(paginator.num_pages)


def process_query(q, c):
    '''Constructs a queryset.

    Returns a list of objects that satisfies the query.'''
    qset = (
        Q(title__icontains=q) |
        Q(language__icontains=q) |
        Q(authors__first_name__icontains=q) |
        Q(authors__last_name__icontains=q) |
        Q(categories__name__icontains=q)
        )
    return c.objects.filter(qset).distinct()
