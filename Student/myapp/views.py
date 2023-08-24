from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import student, Patient_ob

def savevalue(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        pno= request.POST.get('pno')
        age= request.POST.get('age')
        weight= request.POST.get('weight')
        height= request.POST.get('height')
        bgroup= request.POST.get('bgroup')
        gender= request.POST.get('gender')
        print(name)
        post=student(name=name, email=email, pno=pno, age=age, weight=weight, height=height, bgroup=bgroup, gender=gender)
        post.save()
        return render(request, 'register.html', {})  # Redirect after successful form submission


def observations(request):
    if request.method == 'POST':
        observations= request.POST.get('observations')
        id = request.POST.get('userid')

        std = student.objects.get(id=id)
        std.status = True
        std.save()
        post=Patient_ob(observations=observations)
        post.save()
        return render(request, 'register.html', {})


def index(request):
    return render(request, 'index.html', {})

def register(request):
    return render(request, 'register.html', {})

def regbutton(request):
    return render(request, 'regbutton.html', {})

def consult(request):
    records = student.objects.filter(status = False)
    return render(request, 'consult.html', {'records': records})

def proceed(request, record_id):
    record_id = student.objects.get(pk=record_id)
    return render(request, 'proceed.html', {'record_id': record_id})

