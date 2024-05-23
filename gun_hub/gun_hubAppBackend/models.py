from django.db import models
from django.db.models import Model

# Create your models here.
class Cal(models.Model):
    cal = models.CharField(max_length=50)

    def __str__(self):
        return self.cal




class Company(models.Model):
    com = models.CharField(max_length=50)

    def __str__(self):
        return self.com


    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.category_name




class Product(models.Model):
    name = models.CharField(max_length=50)
    cal = models.ForeignKey(Cal, on_delete = models.CASCADE, null=True)
    com = models.ForeignKey(Company, on_delete = models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    image = models.ImageField(null = True, blank = True, upload_to="images/" )
    year = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name} {self.cal} {self.com} {self.category} {self.image} {self.year}'

