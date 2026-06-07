from django.db import models
from django.contrib.auth.models import User
import string, random

def generate_short_code(length=6):

    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))

        if not ShortURL.objects.filter(short_code=code).exists():
            return code


class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="short_urls")
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=15, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_code}={self.original_url}"
    
