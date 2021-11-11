from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

admin.site.register(Users)
UserAdmin.fieldsets += ("Custom fields set",{'fields':('phone_number','birdth_day','sex')}),


