from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Cal, Category, Company, Product


class CalAdmin(admin.ModelAdmin):
    list_display = ["cal"]

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["com"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "cal", "com", "category","image", "year"]


# Register your models here.
admin.site.register(Cal, CalAdmin)
admin.site.register(Category)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
