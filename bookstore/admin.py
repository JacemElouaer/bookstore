from django.contrib import admin

# Register your models here.


from . models import Customer, Order, Book, Tag

admin.site.register([Customer ,  Order , Book, Tag])
