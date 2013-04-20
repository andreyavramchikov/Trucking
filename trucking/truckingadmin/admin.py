from django.contrib import admin
from truckingadmin.models import Driver, Truck, Loader, Customer, OrderStatus, Order, CapacityCatalog, PriceRegister

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(Loader)
admin.site.register(Customer)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(CapacityCatalog)
admin.site.register(PriceRegister)
