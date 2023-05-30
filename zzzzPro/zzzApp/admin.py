

# Register your models here.
# from django.contrib import admin
#from .models import products
# # Register your models here.


from django.contrib import admin
from .models import Products
from .models import Category
#admin.site.register(products)
#from .models import Customer
#from .models import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
#admin.site.register(Customer)
#admin.site.register(Order)
