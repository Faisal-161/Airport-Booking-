from django.contrib import admin

from Flight.models import Flight

class AdminFlight(admin.ModelAdmin):
    list_display = ['aeroplane','departure',
                   'max_passengers']
    list_filter = ['aeroplane','destination','max_passengers', 'departure']

    search_fields =['departure']
     

admin.site.register(Flight, AdminFlight)
# Register your models here.
