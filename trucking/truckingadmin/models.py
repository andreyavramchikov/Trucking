# -*- coding: utf-8 -*-
from django.db import models

LABOR_CATEGORY_CHOICES = (
    ('J', 'First'),
    ('MJ', 'Second'),
    ('M', 'Third'),
    ('S', 'Forth'),
)

class Driver(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=9, unique=True)
    employment_record_number = models.CharField(max_length=8, unique=True)
    labor_category = models.IntegerField()
    number_personal_affairs = models.IntegerField()

    def __unicode__(self):
        return self.surname;


class Truck(models.Model):
    brand = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=9)
    vehicle_inspection = models.CharField(max_length=255)
    released_year = models.DateTimeField()
    carrying_capacity = models.IntegerField()
    holding_capacity = models.IntegerField()
    driver = models.OneToOneField(Driver)

    def __unicode__(self):
        return self.registration_number;

class Loader(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=9, unique=True)

    def __unicode__(self):
        return self.surname;


class Customer(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=9, unique=True)
    telephone_number = models.IntegerField()
    email = models.EmailField()

    def __unicode__(self):
        return self.surname;

class OrderStatus(models.Model):
    agreement_sign = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)
    realization = models.BooleanField(default=False)

class Order(models.Model):
    date_begin_moving = models.DateTimeField(verbose_name='Дата начала поездки')
    date_end_moving = models.DateTimeField(verbose_name="Дата окончания поездки")
    distance = models.IntegerField(verbose_name="Расстояние")
    address_start = models.CharField(max_length=255, verbose_name="Адресс начала поездки")
    address_end = models.CharField(max_length=255, verbose_name="Адресс окончания поездки")
    weight = models.IntegerField(verbose_name="Вес")
    volume = models.IntegerField(verbose_name="Объем")
    price = models.IntegerField(verbose_name="Цена")

    order_status = models.OneToOneField(OrderStatus, verbose_name="Статус заказа")
    customer = models.ForeignKey(Customer, verbose_name="Клиент")
    truck = models.ManyToManyField(Truck, verbose_name="Автомобили")
    loader = models.ManyToManyField(Loader, verbose_name="Грузчики")


class CapacityCatalog(models.Model):
    name = models.CharField(max_length=40, unique=True)
    average_weight = models.IntegerField()
    average_volume = models.IntegerField()

    def __unicode__(self):
        return self.name;


class PriceRegister(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name;
