from django.contrib import admin

# Register your models here.
from .models import Course, Test, Question


class TestInline(admin.StackedInline):
    model = Test
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    inlines = [TestInline]

#TODO: How to add Question inline?

admin.site.register(Course, CourseAdmin)