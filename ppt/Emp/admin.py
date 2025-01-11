from django.contrib import admin

# Register your models here.
from .models import emp,Testimonial
class EmpAdmin(admin.ModelAdmin):

   list_display=['name','emp_mail','status','department','phone_number']
   list_editable=['status',]
   search_fields=['name','emp_mail']
   list_filter=['status',]
admin.site.register(emp,EmpAdmin)
admin.site.register(Testimonial)
