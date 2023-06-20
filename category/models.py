from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 20, unique = True)
    description = models.CharField(max_length = 255, blank = True)
    slug = models.CharField(max_length = 100, unique = True)
    # Para manejar el upload de archivos en djnago toca instalar pillow "pip install pillow"
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        # http://localhost:8000/store/ropa-de-verano
        return reverse("products_by_category", args=[self.slug])
    
    def __str__(self):
        return self.category_name