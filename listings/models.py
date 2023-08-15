# from django.db import models
# from datetime import datetime
# from seller.models import Seller

# class Listing(models.Model):
#     seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
#     title = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=20)
#     description = models.TextField(blank=True)
#     price = models.IntegerField()
#     engine_size = models.IntegerField()
#     horse_power = models.IntegerField()
#     mileage = models.FloatField()
#     weight = models.FloatField()
#     torque = models.FloatField()
#     category = models.CharField(max_length=15)
#     fuel_type = models.CharField(max_length=10)
#     make_date = models.DateTimeField()
#     photo_main = models.ImageField(upload_to= 'photos/%Y/%m/%d/')
#     photo_1 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
#     photo_2 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
#     photo_3 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
#     photo_4 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
#     photo_5 = models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank = True)
#     is_published = models.BooleanField(default=True)
#     list_date = models.DateTimeField(default=datetime.now, blank=True)
#     def __str__(self):
#         return self.title


from django.db import models
from datetime import datetime
from seller.models import Seller
from django.utils import timezone


class Listing(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    engine_size = models.FloatField()
    horse_power = models.IntegerField()
    mileage = models.FloatField()
    weight = models.FloatField()
    torque = models.FloatField()
    category = models.CharField(max_length=15)
    fuel_type = models.CharField(max_length=10)

    # Change make_date to only store the year
    # make_date = models.PositiveIntegerField()
    make_date = models.DateField(default=timezone.now(
    ).date(), blank=True)  # The final desired state

    # Change photo fields to allow them to be null
    photo_main = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', null=True, blank=True)

    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=timezone.now().date(), blank=True)

    def __str__(self):
        return self.title
