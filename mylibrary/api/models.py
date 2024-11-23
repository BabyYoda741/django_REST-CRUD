from django.db import models

# Create your models here.
class Books(models.Model):
    bookID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    average_rating = models.FloatField()
    isbn = models.IntegerField()
    isbn13 = models.IntegerField()
    language_code = models.CharField(max_length=200)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date  = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)