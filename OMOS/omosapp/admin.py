from django.contrib import admin

# Register your models here.
from omosapp.models import *

admin.site.register(SystemUser)
admin.site.register(Address)
admin.site.register(ClientItem)
admin.site.register(ClientCategory)
admin.site.register(ClientRate)
admin.site.register(ClientTag)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Chart)
