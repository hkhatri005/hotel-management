from django.contrib import admin
from .models import Customer, ServiceStaff, Bookings, Rooms, Payments

admin.site.register(Customer)
admin.site.register(ServiceStaff)
admin.site.register(Bookings)
admin.site.register(Rooms)
admin.site.register(Payments)



