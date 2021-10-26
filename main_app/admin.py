from django.contrib import admin

# Register your models here.
from .models import Boat, Gear, Owner

# register your models here.
admin.site.register(Boat)
admin.site.register(Gear)
admin.site.register(Owner)
