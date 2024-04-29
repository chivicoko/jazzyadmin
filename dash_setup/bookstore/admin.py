from django.contrib import admin
from .models import Book
import django.apps

section_1_description = "This is the description of section 1..."
section_2_description = "This is the description of section 2..."
class BookstoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('author',)
    list_per_page = 10
    fieldsets = (
        ( 'Section 1', {'fields': ('title',), 'description': f"{section_1_description}", 'classes': ('collapse',), } ),
        ( 'Section 2', {'fields': ('author', 'isbn'), 'description': f"{section_2_description}", 'classes': ('collapse',), } ),
    )

class BookstoreAdminArea(admin.AdminSite):
    site_header = 'Bookstore Admin Area'
    site_title = 'Bookstore Admin Page'
    index_title = "Bookstore Panel"

bookstore_site = BookstoreAdminArea(name='BookstoreAdmin')

bookstore_site.register(Book, BookstoreAdmin)
admin.site.register(Book, BookstoreAdmin)


# Just extra stuff
# registeration all existing models
allModels = django.apps.apps.get_models()
# print(allModels)

for model in allModels:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# to unregister some models we don't want in the admin site
admin.site.unregister(django.contrib.admin.models.LogEntry)
admin.site.unregister(django.contrib.auth.models.Permission)
admin.site.unregister(django.contrib.contenttypes.models.ContentType)
admin.site.unregister(django.contrib.sessions.models.Session)
