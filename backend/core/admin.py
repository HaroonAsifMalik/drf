from django.contrib import admin

# Register your models here.
# ----m3-----
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'email')
