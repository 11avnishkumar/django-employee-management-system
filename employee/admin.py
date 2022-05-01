from django.contrib import admin
from .models import (Employee,Upload_employee_details)

admin.site.register(Employee)
admin.site.register(Upload_employee_details)
# we have created two admin.site.register seprately otherwise
# it will give error url not found
