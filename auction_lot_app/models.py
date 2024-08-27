from django.db import models
from datetime import timedelta, datetime
from django.utils.timezone import now
from django.contrib.auth.models import User


class AuctionLot(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)

    # write func that checks if end_price > start_price
    end_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True)

    # SUGGESTION: write func that checks if end_date > start_date

    # SUGGESTION: How to upload multiple images?
    # SUGGESTION: image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:

            # add 30 days to start_date and set it as end_date
            self.end_date = datetime.now() + timedelta(days=30)

            # for the first time saved, set end_price to start_price
            self.end_price = self.start_price
        super().save(*args, **kwargs)


class Bid(models.Model):
    auction_lot = models.ForeignKey(AuctionLot, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.participant} - {self.auction_lot.title} - {self.bid_price}'
