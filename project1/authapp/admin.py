from django.contrib import admin
from .models import (
    Category, Trainer, MembershipPlan, 
    Enrollment, Product, Contact, 
    Gallery, Attendance
)

class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('plan', 'price', 'duration_days', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('plan', 'description')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'Email', 'SelectMembershipplan', 'paymentStatus', 'timeStamp')
    list_filter = ('paymentStatus', 'Gender')
    search_fields = ('FullName', 'Email', 'PhoneNumber')
    readonly_fields = ('timeStamp',)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'email')
    list_filter = ('gender',)
    search_fields = ('name', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_available', 'stock')
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'description')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber')
    search_fields = ('name', 'email', 'phonenumber', 'description')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'timeStamp')
    search_fields = ('title',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('phonenumber', 'Selectdate', 'Login', 'Logout')
    list_filter = ('Selectdate',)
    search_fields = ('phonenumber', 'TrainedBy')

# Register models with their admin classes
admin.site.register(Category)
admin.site.register(MembershipPlan, MembershipPlanAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Attendance, AttendanceAdmin)