from django.contrib import admin

# Register your models here.
from collection.models import Knits


class KnitsAdmin(admin.ModelAdmin):
    model = Knits
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Knits, KnitsAdmin)
