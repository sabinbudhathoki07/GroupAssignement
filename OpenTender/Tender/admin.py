from django.contrib import admin
from Tender.models import USER, POST

class Tender_User(admin.ModelAdmin):
    list_display=('Email', 'Phone_No', 'Company_name')


class Tender_Post(admin.ModelAdmin):
    list_display=('Tender_Name', 'Status', 'Date','Tender_Type','Business_Scale', 'Entry_Fee')

admin.site.register(USER, Tender_User),
admin.site.register(POST, Tender_Post),
