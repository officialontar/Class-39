from django.shortcuts import get_object_or_404, render, redirect
from .models import Student
from django.http import HttpResponse


def home(request):
    return render(request, 'student_info/index.html')


def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        message = request.POST.get('message')
        image = request.FILES.get('profile_pic')

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            tel=tel,
            dob=dob,
            gender=gender,
            profile_pic=image,
            country=country,
            message=message,
        )

        return redirect('all_student')

    return render(request, 'student_info/add_student.html')


def all_student(request):
    student_data = Student.objects.all()
    context = {'data': student_data}
    return render(request, 'student_info/all_student.html', context)


def content(request):
    return render(request, 'student_info/content.html')


def detele_student(request, std_id):

    # student = Student.objects.filter(id=std_id)
    # student.delete()

    student = get_object_or_404(Student, id=std_id)

    student.delete()

    return redirect('all_student')



def edit_student(request, std_id):

    student_data = get_object_or_404(Student, id=std_id)

    if request.method == "POST":
        student_data.first_name = request.POST.get('first_name')
        student_data.last_name = request.POST.get('last_name')
        student_data.email = request.POST.get('email')
        student_data.tel = request.POST.get('tel')
        student_data.dob = request.POST.get('dob')
        student_data.gender = request.POST.get('gender')

        if request.FILES.get('profile_pic'):
            if student_data.profile_pic:
                student_data.profile_pic.delete(save=False)
            student_data.profile_pic = request.FILES.get('profile_pic')


        student_data.country = request.POST.get('country')
        student_data.message = request.POST.get('message')

        student_data.save()
        return redirect('all_student')



    context = {
        'student' : student_data
    }

    return render(request, 'student_info/edit_student.html', context)


def view_student(request, std_id):
    student_data = get_object_or_404(Student, id=std_id)
    context = {'student': student_data}
    return render(request, 'student_info/view_student.html', context)