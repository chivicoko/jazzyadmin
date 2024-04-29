from django.db import models

class Profiler(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    is_approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"