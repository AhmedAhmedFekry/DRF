from django.db import models

# Create your models here.
class Category(models.Model):
    
    title = models.CharField(
        max_length=50,
        verbose_name="title",
    )

class Product(models.Model):
  
    category = models.ForeignKey(
        Category,
        related_name="categoryProduct",
        on_delete=models.CASCADE,
        verbose_name="category",
    )
    title = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="title"
    )
    
    image = models.ImageField(
        upload_to="images/",
       
        blank=True,
        null=True,
        verbose_name="image",
    )
    def __str__(self):
        return str(self.title)
