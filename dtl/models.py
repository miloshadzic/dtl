from django.db import models

# Create your models here.

YEARS = [ ( i+1960, i+1960) for i in range(80) ]

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.last_name + ", " + self.first_name

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    isbn = models.IntegerField(max_length=13)
    title = models.CharField(max_length=100)
    pub_date = models.IntegerField(max_length=4, choices=YEARS)

    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

