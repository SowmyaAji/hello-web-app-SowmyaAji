from django.contrib import admin

# Register your models here.
from collection.models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'description', 'picture')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, BookAdmin)
