from django.db import models

# Create your models here.


class AuctionLot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)

    # write func that checks if end_price > start_price
    end_price = models.DecimalField(max_digits=10, decimal_places=2)

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()  # write func that checks if end_date > start_date

    # How to upload multiple images?
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
