from django.shortcuts import render
from student.models import *
def home_page(request):
    return render(request,"home.html")
def teacher_page(request):
    techer_data = TeacherModel.objects.all()
    context = {
        "teacher_data": techer_data
    }
    return render(request,"teacher.html",context)
def student(request):
    student_data = StudentModel.objects.all()
    context = {
        "student_data": student_data
    }
    return render(request,"student.html",context)
def Dept_page(request):
    dept_data = Dept.objects.all()
    context = {
        "dept_data": dept_data
    }
    return render(request,"dept.html",context)
def course_page(request):
    course_data = CourseModel.objects.all()
    context = {
        "course_data": course_data
    }
    return render(request,"course.html",context)
def exam_page(request):
    exam_data = ExamModel.objects.all()
    context = {
        "exam_data": exam_data
    }
    return render(request,"exam.html",context)
def classroom_page(request):
    classroom_data = ClassroomModel.objects.all()
    context = {
        "classroom_data": classroom_data
    }
    return render(request,"classroom.html",context)
def attendance_page(request):
    att_data = AttendanceModel.objects.all()
    context = {
        "att_data": att_data
    }
    return render(request,"attendance.html",context)
    