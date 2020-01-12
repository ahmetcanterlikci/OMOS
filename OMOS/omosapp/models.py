from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    is_client = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    clientType = models.CharField(max_length=50, null=True, blank=True)
    clientFax = models.CharField(max_length=50, null=True, blank=True)
    clientAddress = models.TextField(null=True, blank=True)
    clientDistrict = models.CharField(max_length=50, null=True, blank=True)
    clientNeighborhood = models.CharField(max_length=50, null=True, blank=True)
    clientMinPrice = models.BigIntegerField(null=True, blank=True)
    clientAvgTime = models.CharField(max_length=50, null=True, blank=True)
    clientManagerEmail = models.CharField(max_length=50, null=True, blank=True)
    clientrate = models.IntegerField(null=True, blank=True)
    customerCount = models.IntegerField(null=True, blank=True)
    clientName = models.TextField(unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    clientTags = models.TextField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            SystemUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.systemuser.save()


class ClientItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('ClientCategory', null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "category"),)


class ClientCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    item1 = models.TextField(null=True, blank=True)
    price1 = models.CharField(max_length=20, null=True, blank=True)
    item2 = models.TextField(null=True, blank=True)
    price2 = models.CharField(max_length=20, null=True, blank=True)
    item3 = models.TextField(null=True, blank=True)
    price3 = models.CharField(max_length=20, null=True, blank=True)
    item4 = models.TextField(null=True, blank=True)
    price4 = models.CharField(max_length=20, null=True, blank=True)
    item5 = models.TextField(null=True, blank=True)
    price5 = models.CharField(max_length=20, null=True, blank=True)
    item6 = models.TextField(null=True, blank=True)
    price6 = models.CharField(max_length=20, null=True, blank=True)
    item7 = models.TextField(null=True, blank=True)
    price7 = models.CharField(max_length=20, null=True, blank=True)
    item8 = models.TextField(null=True, blank=True)
    price8 = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        unique_together = (("name", "user"),)


class ClientTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.CharField(max_length=100)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    clientUsername = models.CharField(max_length=100, null=True)
    order_date = models.DateTimeField(default=timezone.now)
    itemName = models.TextField(null=True)
    itemPrice = models.CharField(max_length=20, null=True)
    itemCount = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=50)
    clientName = models.CharField(max_length=100, null=True)
    orderNumber = models.CharField(max_length=100, null=True)
    clientAddress = models.TextField(null=True)


class OrderDetail(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    clientItem = models.ForeignKey('ClientItem', null=True, on_delete=models.CASCADE)
    amount = models.BigIntegerField()

    class Meta:
        unique_together = (("order", "clientItem"),)


class Chart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    clientName = models.CharField(max_length=100, null=True)
    itemName = models.TextField(null=True)
    itemPrice = models.CharField(max_length=20, null=True)
    itemCount = models.CharField(max_length=20, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    clientNameText = models.CharField(max_length=100, null=True, blank=True)


class NavigationContent(models.Model):
    usertype = models.TextField(null=True)
    path = models.TextField()
    name = models.TextField()


class MyProfileContent(models.Model):
    usertype = models.TextField(null=True)
    path = models.TextField()
    name = models.TextField()
    faicon = models.TextField(null=True)





