
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import UploadFile
from .forms import ResumeForm
from django.http import FileResponse


     

# def login_user(request):
#     if request.method=='POST':
#         username=request.POST.get('username','').strip()
#         password=request.POST.get('password','').strip()

#         if not username or not password:
#             messages.error(request,'both username and password are required')
#         else:
#             user=authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,f'welcom back{user.username}!')
#                 return redirect('home')
#             else:
#                 messages.error(request,'invalid username or password')

#     return render(request,'login.html') 
from django.shortcuts import render, redirect
from django.contrib import messages




def home(request):
    return render(request,'home.html')         



def home(request):
    return render(request,'home.html')

def report(request):
    return render(request,'report.html')
     
def upload2(request):
    files = UploadFile.objects.all()

    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload2')
    else:
        form = ResumeForm()

    return render(request, 'upload2.html', {'form': form, 'files': files})     

def view_file(request, file_id):
    file_obj = get_object_or_404(UploadFile, id=file_id)
    file_path = file_obj.file.path
    return FileResponse(open(file_path, 'rb'))

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        country = request.POST.get("country")    # ← Get country from form

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signup")

        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create user profile WITH country field
        UserProfile.objects.create(
            user=user,
            country=country
        )

        messages.success(request, "Signup successful! Please login.")
        return redirect("signin")

    return render(request, "signup1.html")


from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request,username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "login.html")
