from django.contrib import admin
from .models import *
from .models import TopNote
# Register your models here.

admin.site.register(Contact)
admin.site.register(Item)
admin.site.register(TopNote)
admin.site.register(Reservation)