from dtl.models import *
from django.contrib import admin


class AuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Book.categories.through
    extra = 1


class CopyAdminInline(admin.TabularInline):
    model = Book.copies
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name']
    list_display_links = ['pk']
    list_editable = ['first_name', 'last_name']


class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'isbn', 'pub_date', 'language')
    inlines = [AuthorInline, CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk']
    list_editable = ['name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BookCopy)
admin.site.register(Book, BookAdmin)
admin.site.register(BookReservation)
admin.site.register(BookOnLoan)
admin.site.register(User)
