from django.shortcuts import render, redirect
from .models import Course,Student
from django.contrib import messages

def home_view(request):
    return render(request,"home.html")

def add_course_view(request):
    courses = Course.objects.all()
    if request.method == "POST":
        cname = request.POST.get('cname')
        fee = int(request.POST.get('fee'))
        duration = request.POST.get('duration')


        # Validation
        if not cname:
            messages.error(request, "Course name is mandatory")
        elif Course.objects.filter(cname=cname).exists():
            messages.error(request, "Course Name is already registered")
        elif not fee or fee <= 0:
            messages.error(request, "Fee must be positive Integer")
        else:
            Course.objects.create(cname=cname, fee=fee, duration=duration)
            messages.success(request, f"Course {cname} is added successfully ")
            return redirect('home')
    return render(request, 'addcourse.html', context={"courses": courses})





def register_student_view(request):
    courses = Course.objects.all()
    students = Student.objects.all()


    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        # Get multiple selected courses
        course_ids = request.POST.getlist('courses')
        qualification = request.POST.get('qualification')


        # Validation
        if not name:
            messages.error(request, "Name is mandatory")
        elif not email:
            messages.error(request, "Email is mandatory")
        elif Student.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
        elif not course_ids:
            messages.error(request, "Please select at least one course")
        else:
            # Create student
            student = Student.objects.create(
                name=name,
                email=email,
                address=address,
                gender=gender,
                qualification=qualification
            )
            # Add selected courses
            student.courses.set(course_ids)
            messages.success(request, f"Student {name} registered successfully with Roll No: {student.roll}")
            return redirect('home')
    return render(request, 'registerstudent.html', context={'courses': courses, 'students': students})




def course_student_list_view(request, course_id):
    course = Course.objects.get(course_id=course_id)
    students = course.student_set.all()  # Get all students enrolled in this course
    return render(request, 'coursestudentlist.html', context={'course': course, 'students': students})

def delete_course_view(request, course_id):
    course = Course.objects.get(course_id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(
            request, f"Course {course.cname} deleted successfully")
        return redirect('addcourse')
    return render(request, 'deletecourse.html', context={'course': course})



def update_course_view(request, course_id):
    course = Course.objects.get(course_id=course_id)
    if request.method == "POST":
        cname = request.POST.get('cname')
        fee = int(request.POST.get('fee'))
        duration = request.POST.get('duration')


        # Validation
        if not cname:
            messages.error(request, "Course name is mandatory")
        elif Course.objects.filter(cname=cname).exclude(course_id=course_id).exists():
            messages.error(request, "Course Name is already registered")
        elif not fee or fee <= 0:
            messages.error(request, "Fee must be a positive integer")
        else:
            course.cname = cname
            course.fee = fee
            course.duration = duration
            course.save()
            messages.success(request, f"Course {cname} updated successfully")
            return redirect('addcourse')
    return render(request, 'updatecourse.html', context={'course': course})
