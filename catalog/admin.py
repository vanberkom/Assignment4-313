from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)


class BooksInline(admin.TabularInline):
    model = Book
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
