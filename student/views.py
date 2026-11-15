from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Department,Student

# Create your views here.
def register(request):
    if request.method == "POST":
        username=request.POST.get('usernaame')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirm password')

    #    password validation
        if password != confirmpassword:
            message.error(request,"password do not match")
            return redirect('register')

            # check username already exist
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exist!!")
            return redirect('register')

            # check email already exist
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exist!!")
            return redirect('register')

            # create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request,"Registration successful")
        return redirect('login')
    return render(request,'register.html')


def user_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('login')
    return render(request,'login.html')


@login_required
def dashboard(request):
    return render(request,'dashboard.html')



@login_required
def add_department(request):
    if request.method == "POST":
        dept_name=request.POST.get('DepartmentName')
        description=request.POST.get('Description')

        Department.objects.create(dept_name=dept_name,description=description)
        return redirect('dashboard')
    return render(request,'add_department.html')

@login_required
def view_department(request):
    departments=Department.objects.all()
    return render(request,'view_department.html',{'departments':departments})

@login_required
def edit_department(request,id):
    department=Department.objects.get(id=id)
    if request.method == "POST":
        department.department_name=request.POST.get('department_name')
        department.description=request.POST.get('description')
        department.save()
        return redirect('view_department')
    return render(request,'edit_department.html',{'department':department})

@login_required(login_url='/login/')
def delete_department(request,id):
    department=Department.objects.get(id=id)
    department.delete()
    return redirect('view_department')
    # return redirect('view_department')

def add_student(request):
    if request.method == "POST":
        username=request.POST.get("username")
        name=request.POST.get('name')
        course=request.POST.get('course')
        email=request.POST.get("email")
        password=request.POST.get("password")
        department_id=request.POST.get('department')
# check username
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exist!!")
            return redirect('add_student')
        # check email
        if User.objects.filter(email=email).exists():
           messages.error(request,"Email already exist!!")
           return redirect('add_student')
# create user
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
                # get department
        department=Department.objects.get(id=department_id)
        # create Student
        Student.objects.create(
            user=user,
            name=name,
            course=course,
            department=department
        )
        messages.success(request,"student added successfully!!")
        return redirect('add_student')
    departments=Department.objects.all()
    print("===DEBUG ===")
    for d in departments:
        print("ID",d.id,"Name:",d)
    print("===============")
    return render(request,'add_student.html',{'departments':departments})

@login_required
def view_student(request):
    students= Student.objects.all()
    return render(request,'view_student.html',{'students':students})

@login_required
def edit_student(request,id):
    student=Student.objects.get(id=id)
    departments=Department.objects.all()
    if request.method == "POST":
        student.name=request.POST.get('name')
        student.course=request.POST.get('course')
        department_id=request.POST.get('department')
        department=Department.objects.get(id=department_id)
        student.department=department
        student.save()
        messages.success(request,"Student update")
        
        return redirect('view_student')
    return render(request,'edit_student.html',{'student':student,'departments':departments})

@login_required
def delete_student(request,id):
    student=Student.objects.get(id=id)
    if request.method == "POST":
        student.user.delete()
        return redirect('view_student')
    return redirect('view_student')

def my_profile(request):
    return render(request,'my_profile.html')

def user_logout(request):
    logout(request)
    return redirect('login')









