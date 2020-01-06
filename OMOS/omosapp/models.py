from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models import CharField
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
    tags = models.ManyToManyField('ClientTag', blank=True)
    clientrate = models.IntegerField(null=True)
    customerCount = models.IntegerField(null=True)
    clientName = models.TextField(unique=True, null=True)
    address = models.TextField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            SystemUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.systemuser.save()


class ClientItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    category = models.ForeignKey('ClientCategory', null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "name", "category"),)


class ClientCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (("name", "user"),)


class ClientTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.CharField(max_length=100)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    clientName = models.CharField(max_length=100, null=True)
    date = models.DateTimeField()
    price = models.BigIntegerField()
    paymentMethod = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class OrderDetail(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    clientItem = models.ForeignKey('ClientItem', null=True, on_delete=models.CASCADE)
    amount = models.BigIntegerField()

    class Meta:
        unique_together = (("order", "clientItem"),)


class Chart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    clientItem = models.ForeignKey('ClientItem', null=True, on_delete=models.CASCADE)
    clientName = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = (("customer", "clientItem", "clientName"),)


class NavigationContent(models.Model):
    usertype = models.TextField(null=True)
    path = models.TextField()
    name = models.TextField()


class MyProfileContent(models.Model):
    usertype = models.TextField(null=True)
    path = models.TextField()
    name = models.TextField()
    faicon = models.TextField(null=True)




