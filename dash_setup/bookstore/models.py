from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    isbn = models.IntegerField(help_text='This is more like the ID of this book')

    def __str__(self) -> str:
        return f"{self.title}"