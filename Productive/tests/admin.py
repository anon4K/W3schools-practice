from django.contrib import admin
from .models import TestModel


# Register your models here.
class TestAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", 'sex', "join_date", "phone")

admin.site.register(TestModel, TestAdmin)

class House(TestModel):
    pass

