from django.contrib import admin
from .models import AuctionLot, Bid

# Register your models here.
admin.site.register(AuctionLot)
admin.site.register(Bid)
