from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    is_client = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    clientType = models.CharField(max_length=50, null=True)
    clientFax = models.CharField(max_length=50, null=True)
    clientAddress = models.TextField(null=True)
    clientDistrict = models.CharField(max_length=50, null=True)
    clientNeighborhood = models.CharField(max_length=50, null=True)
    clientMinPrice = models.BigIntegerField(null=True)
    clientAvgTime = models.CharField(max_length=50, null=True)
    clientManagerEmail = models.CharField(max_length=50, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            SystemUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.systemuser.save()


class Address(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)

    class Meta:
        unique_together = (("name", "user"),)


class ClientItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    category = models.CharField(max_length=50)

    class Meta:
        unique_together = (("user", "name"),)


class ClientCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (("name", "user"),)


class ClientRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    rate = models.BigIntegerField()
    customerCount = models.BigIntegerField()


class ClientTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.CharField(max_length=100)

    class Meta:
        unique_together = (("user", "tag"),)


class Order(models.Model):
    orderID = models.BigIntegerField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    clientUsername = models.CharField(max_length=100, null=True)
    date = models.DateTimeField()
    price = models.BigIntegerField()
    paymentMethod = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class OrderDetail(models.Model):
    orderID = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.BigIntegerField()

    class Meta:
        unique_together = (("orderID", "item"),)


class Chart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    clientItemName = models.ForeignKey('ClientItem', on_delete=models.CASCADE)
    clientUsername = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = (("customer", "clientItemName","clientUsername"),)




