from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_SELECTION = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=17, blank=True, null=True)
    telegram = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True)

    def __str__(self):
        return str(self.username)


class Saved(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment of " + str(self.author.username) + " for " + self.product.title