from django.db import models
from django.contrib import admin
class football (models.Model):
    eid=models.CharField(max_length=20,help_text="football ID")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class footballAdmin(admin.ModelAdmin):
    list_display=('eid','name','salary','age','email')
