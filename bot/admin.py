from django.contrib import admin

from .models import User, Flower, Courier, Florist, Order


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    fields = ('full_name', 'chat_id', 'phone_number', 'balance', 'access', 'admin')


@admin.register(Flower)
class AdminFlower(admin.ModelAdmin):
    fields = ('title', 'description', 'type', 'image', 'florist', 'price')


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    fields = ('user', 'flower', 'courier', 'address', 'delivery_date', 'count')


@admin.register(Courier)
class AdminCourier(admin.ModelAdmin):
    fields = ('full_name', 'chat_id')


@admin.register(Florist)
class AdminFlorist(admin.ModelAdmin):
    fields = ('full_name', 'chat_id')
