# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'timestamp', 'profile')



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comments', 'timestamp')



@admin.register(serviceCategories)
class ServiceCategoriesAdmin(admin.ModelAdmin):
    list_display = ['catename', 'category']



@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'cate', 'desc', 'duration', 'price', 'ServicePhoto', 'available', 'timestamp']


@admin.register(serviceInquiry)
class ServicesInquiryAdmin(admin.ModelAdmin):
    list_display = ['user', 'serviceId', 'subject', 'message', 'timestamp']



@admin.register(courcesCategories)
class courcesCategoriesAdmin(admin.ModelAdmin):
    list_display = ['catename', 'category']


@admin.register(Cource)
class courcesAdmin(admin.ModelAdmin):
    list_display = ['name','cate','desc', 'duration', 'price', 'timings','totalStudents', 'CourcePhoto', 'available', 'timestamp']


@admin.register(courceInquiry)
class courceInquiryAdmin(admin.ModelAdmin):
    list_display = ['user', 'courceId', 'subject', 'message', 'timestamp']


