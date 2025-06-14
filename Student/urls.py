from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('addcourse/', views.add_course_view, name='addcourse'),
    path('registerstudent/', views.register_student_view, name='registerstudent'),
    path('course/<int:course_id>/students/',views.course_student_list_view, name='course_student_list'),
    path('course/<int:course_id>/delete/',views.delete_course_view, name='delete_course'),
    path('course/<int:course_id>/update/',views.update_course_view, name='update_course'),
]
