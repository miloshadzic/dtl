from dtl.models import Book, Author,Category
from django.contrib import admin

class AuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1

class CategoryInline(admin.TabularInline):
    model = Book.categories.through
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name']
    list_display_links = ['pk']
    list_editable = ['first_name', 'last_name']

class BookAdmin(admin.ModelAdmin):
    fields =('title', 'isbn')
    inlines = [ AuthorInline, CategoryInline ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk','name']
    list_display_links = ['pk']
    list_editable = ['name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
