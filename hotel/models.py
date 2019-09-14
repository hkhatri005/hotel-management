from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_id)


class ServiceStaff(models.Model):
    staff_id = models.AutoField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return str(self.staff_id)


class Payments(models.Model):
    payment_id = models.AutoField(max_length=50, primary_key=True)
    total_amount = models.FloatField(max_length=50)
    payment_timestamp = models.DateTimeField(
        default=timezone.now)

    def created(self):
        self.payment_timestamp = timezone.now()
        self.save()

    def __str__(self):
        return str(self.payment_id)


class Bookings(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE, related_name='payment')
    booking_id = models.AutoField(max_length=50, primary_key=True)
    checkin_timestamp = models.DateTimeField(
        default=timezone.now)
    checkout_timestamp = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.checkin_timestamp = timezone.now()
        self.save()

    def updated(self):
        self.checkout_timestamp = timezone.now()
        self.save()

    def __str__(self):
        return str(self.booking_id)



class Rooms(models.Model):
    booking_id = models.ForeignKey(Bookings, on_delete=models.CASCADE, related_name='booking')
    staff_id = models.ForeignKey(ServiceStaff, on_delete=models.CASCADE, related_name='service')
    room_number = models.CharField(max_length=10, primary_key=True)
    room_type = models.CharField(max_length=20)
    room_charge = models.FloatField(max_length=50)

    def __str__(self):
        return str(self.room_number)