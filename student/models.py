from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
class StudentModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    roll = models.IntegerField()
class Dept(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)
    office_number = models.CharField(max_length=200)
class CourseModel(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    credit = models.IntegerField()
class ExamModel(models.Model):
    subject = models.CharField(max_length=200)
    subject = models.DateField()    
    totallmarks = models.IntegerField()
class ClassroomModel(models.Model):
    room_number = models.CharField(max_length=200)
    capacity = models.IntegerField()
    building = models.CharField(max_length=200)
class AttendanceModel(models.Model):
    student_name = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=200)
    
    