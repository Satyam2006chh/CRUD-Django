from django.contrib import admin
from .models import Course, Student
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'cname', 'fee', 'duration')  # Display columns
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender','qualification', 'enrolled_courses')

    radio_fields = {'gender': admin.HORIZONTAL}


    def enrolled_courses(self, obj):
        course_names = []
        for course in obj.courses.all():
            course_names.append(course.cname)
        return ", ".join(course_names)


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)