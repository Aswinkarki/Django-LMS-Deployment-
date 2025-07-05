# Students/admin.py
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'created_date', 'updated_date']
    search_fields = ['student_name']
    ordering = ['student_name']

admin.site.register(Student, StudentAdmin)
