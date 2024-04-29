from django.apps import AppConfig
# from django.contrib.admin.apps import AdminConfig


# class BookstoreAdminConfig(AdminConfig):
#     default_site = 'bookstore.admin.BookstoreAdminArea'


class BookstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookstore'
