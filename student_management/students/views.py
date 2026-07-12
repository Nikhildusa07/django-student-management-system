from django.shortcuts import render, redirect
from .models import Student


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        course = request.POST.get("course")
        city = request.POST.get("city")
        fees = request.POST.get("fees")

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            course=course,
            city=city,
            fees=fees
        )

        return redirect("/")

    students = Student.objects.all()

    return render(
        request,
        "home.html",
        {"students": students}
    )


def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")
        student.course = request.POST.get("course")
        student.city = request.POST.get("city")
        student.fees = request.POST.get("fees")

        student.save()

        return redirect("/")

    return render(
        request,
        "update.html",
        {"student": student}
    )

def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect("/")