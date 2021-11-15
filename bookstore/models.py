from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=8)
    age = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    CATEGORY = (
        ("Classics", "Classics"),
        ("Comic Book or Graphic Novel", "Comic Book or Graphic Novel"),
        ("Fantasy", "Fantasy"),
        ("Historical Fiction", "Historical Fiction"),
        ("Horror", "Horror"),
        ("Literary Fiction", "Literary Fiction")
    )
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.FloatField(null=False)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=300, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
        ("Out of order", "Out of order"),
        ("In progress", "In progress"),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, max_length=1200)
    date_created = models.DateField(auto_now_add=True, null=False)
    status = models.CharField(null=False, max_length=200, choices=STATUS)

    def __int__(self):
        return self.id

# Create your models here.
