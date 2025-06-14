from django.db import models

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.cname


class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    QUALIFICATION_CHOICES = (
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('Other', 'Other'),
    )

    roll = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    courses = models.ManyToManyField(Course)
    qualification = models.CharField(max_length=50, choices=QUALIFICATION_CHOICES)

    def __str__(self):
        return self.email
