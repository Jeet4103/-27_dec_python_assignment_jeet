from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm , DoctorEditForm
from .models import Doctor

def home(request):
    doctors = Doctor.objects.all()
    specialties = Doctor.objects.values_list('specialty', flat=True).distinct()
    return render(request, 'home.html', {'doctors': doctors, 'specialties': specialties})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)  

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html') 

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have registered successfully.")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed. Please try logging in.")
        else:
            messages.error(request, "There was a problem signing up. Please try again.")

    return render(request, 'signup.html', {'form': form})

def doctor_detail(request, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        messages.error(request, "Doctor not found.")
        return redirect('home')

    return render(request, 'doctor_detail.html', {'doctor': doctor})


def about(request):
    return render(request, 'about.html')

def get_all_specialties():
    return Doctor.objects.values_list('specialty', flat=True).distinct()

def category_view(request, category_name):
    doctors = Doctor.objects.filter(specialty__iexact=category_name)

    if not doctors.exists():
        messages.error(request, f"No doctors found in the '{category_name}' category.")
        return redirect('home')

    context = {
        'doctors': doctors,
        'category_name': category_name,
        'specialties': get_all_specialties(),
    }
    return render(request, 'category.html', context)



def doctors_admin(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('home')

    doctors = Doctor.objects.all()
    return render(request, 'doctor_admin.html', {'doctors': doctors})



def edit_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == "POST":
        form = DoctorEditForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor details updated successfully.")
            return redirect('doctors_admin')
    else:
        form = DoctorEditForm(instance=doctor)

    return render(request, 'edit_doctor.html', {'form': form, 'doctor': doctor})

def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == "POST":
        doctor.delete()
        messages.success(request, "Doctor deleted successfully.")
        return redirect('doctors_admin')

    return render(request, 'delete_doctor.html', {'doctor': doctor})

def add_doctor(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, "You do not have permission to add a doctor.")
        return redirect('home')

    if request.method == "POST":
        form = DoctorEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor added successfully.")
            return redirect('doctors_admin')
    else:
        form = DoctorEditForm()

    return render(request, 'add_doctor.html', {'form': form})