from django.db import models


class User(models.Model):
    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=50
    )

    chat_id = models.CharField(
        verbose_name='ID TG CHAT',
        max_length=30
    )

    phone_number = models.CharField(
        verbose_name='Номер телефона',
        max_length=30
    )

    balance = models.DecimalField(
        verbose_name='Баланс пользователя',
        decimal_places=2,
        max_digits=5,
        default=0
    )

    admin = models.BooleanField(
        verbose_name='Администратор',
        default=False
    )


class Florist(models.Model):
    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=30
    )
    chat_id = models.CharField(
        verbose_name='ID TG CHAT',
        max_length=30
    )


class Courier(models.Model):
    full_name = models.CharField(
        verbose_name='Полное имя',
        max_length=30
    )
    chat_id = models.CharField(
        verbose_name='ID TG CHAT',
        max_length=30
    )


class Flower(models.Model):
    title = models.CharField(
        verbose_name='Название букета',
        max_length=30
    )

    description = models.TextField(
        verbose_name='Описание букета',
        max_length=100
    )

    type = models.CharField(
        verbose_name='Тип цветов',
        max_length=30
    )

    image = models.ImageField(
        verbose_name='Ссылка на фото'
    )

    florist = models.ForeignKey(
        Florist,
        related_name='florists',
        verbose_name='Флорист',
        on_delete=models.SET_NULL,
        null=True
    )

    price = models.DecimalField(
        verbose_name='Цена букета',
        decimal_places=2,
        max_digits=5,
        default=0
    )


class Order(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_orders',
        verbose_name='Покупатель',
        on_delete=models.CASCADE
    )

    flower = models.ForeignKey(
        Flower,
        related_name='ordered_flowers',
        verbose_name='Букет',
        on_delete=models.SET_NULL,
        null=True
    )

    courier = models.ForeignKey(
        Courier,
        related_name='couriers',
        verbose_name='Курьер',
        on_delete=models.SET_NULL,
        null=True
    )

    address = models.CharField(
        verbose_name='Адрес покупателя',
        max_length=30
    )

    delivery_date = models.DateTimeField(
        verbose_name='Дата доставки',
    )

    count = models.IntegerField(
        verbose_name='Кол-во букетов',
        default=0
    )
