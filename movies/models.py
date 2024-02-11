from django.db import models

# Create your models here.
class Product(models.Model):
    isim = models.CharField(max_length=50)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    resim = models.FileField(upload_to="ürünler/",verbose_name="Ürün Resmi", null=True,blank=True)

    def __str__(self):
        return self.isim
    
    