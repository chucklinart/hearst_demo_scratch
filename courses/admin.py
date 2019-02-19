from django.contrib import admin
from .models import Department, Course, Student, Prof

admin.site.register(Department)

class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('course_title', 'course_description')
    list_select_related = ('department', )

admin.site.register(Course)

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('last_name', 'first_name', 'major')
    list_select_related = ('major', )

admin.site.register(Student, StudentAdmin)

class ProfAdmin(admin.ModelAdmin):
    model = Prof
    list_display = ('last_name', 'first_name')
    list_select_related = ('department', )

admin.site.register(Prof, ProfAdmin)
