from django.db import models
from users.models import CustomUser

class Colors(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
class Sizes(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000000, decimal_places=2)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    color = models.ManyToManyField(Colors)
    url = models.URLField(max_length = 1000, blank=True, null=True)
    seo_keywords = models.TextField()
    seo_description = models.TextField()
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "Comment of " + str(self.author.username) + " for " + self.product.title

class ClotheCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="clothes_category/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seo_keywords = models.TextField()
    seo_description = models.TextField()
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.title)

class Clothes(models.Model):
    category = models.ForeignKey(ClotheCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length = 1000, blank=True, null=True)
    color = models.ManyToManyField(Colors)
    price = models.DecimalField(max_digits=100000000, decimal_places=2)
    seo_keywords = models.TextField()
    seo_description = models.TextField()

    

class ClothesImage(models.Model):
    clothe = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clothes/')