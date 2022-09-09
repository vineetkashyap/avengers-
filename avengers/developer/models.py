from django.db import models


# Create your models here.
class Review(models.Model):
    rating = models.CharField(max_length=50)
    review = models.TextField()
    review_time = models.DateTimeField(auto_now=True)


class Developer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
