from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def student_dashboard(request):
    return render(request, 'student/dashboard.html')

def student_profile(request):
    return render(request, 'student/profile.html')

def student_profile_update(request):
    return render(request, 'student/profile_update.html')

def student_settings(request):
    return render(request, 'student/settings.html')