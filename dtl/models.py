from django.db import models
from datetime import date,timedelta

YEARS = [ ( i+1960, i+1960) for i in range(80) ]
DAYS_ON_LOAN = timedelta(days=15)
LANGUAGES = (
        ('srp', 'Serbian'),
        ('eng', 'English'),
        ('fra', 'French'),
        )

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.last_name + ", " + self.first_name

class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class Book(models.Model):
    isbn = models.IntegerField(max_length=13)
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=30, choices=LANGUAGES)
    pub_date = models.IntegerField(max_length=4, choices=YEARS)
    times_loaned = models.IntegerField(default=0)

    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    student_id = models.CharField(max_length=6, unique=True)
    fonis_id = models.PositiveIntegerField(unique=True)
    email = models.EmailField(max_length=75, unique=True)
    phone = models.CharField(max_length=15)
    other = models.TextField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class BookReservation(models.Model):

    class Meta:
        verbose_name_plural = 'Reservations'

    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    date_reserved = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.user.__unicode__() + " / " + self.book.__unicode__() + " / " + str(self.date_reserved) 

class BookOnLoan(models.Model):

    class Meta:
        verbose_name_plural = 'Loaned Books'

    user = models.ForeignKey(User)
    book = models.ForeignKey(Book, related_name='loaned')

    date_issued = models.DateField(auto_now_add=True)
    date_due = models.DateField(default = date.today() + DAYS_ON_LOAN)
    date_returned = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(BookOnLoan, self).save(*args, **kwargs)
        self.book.times_loaned += 1
        self.book.save()

    def __unicode__(self):
        return self.book.__unicode__() + " / " + self.user.__unicode__() + " / " + str(self.date_due)
