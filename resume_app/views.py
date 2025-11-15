# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from .models import ImgUpload
# from .forms import ImgUploadForm
# def registration(request):
#     if request.method == 'POST':         
#         fullname = request.POST.get('fullname', '').strip()
#         email = request.POST.get('email', '').strip()
#         username = request.POST.get('username', '').strip()
#         password = request.POST.get('password', '').strip()
#         confirm_password = request.POST.get('confirm_password', '').strip()

#         # ✅ validation should be inside this block
#         if not fullname or not email or not password:
#             messages.error(request, 'All fields are required')
#         elif password != confirm_password:
#             messages.error(request, 'Passwords do not match')
#         elif User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists')
#         elif len(fullname) < 3:
#             messages.error(request, 'Full name must have at least 3 letters')
#         elif User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists')
#         else:
#             # create user
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.first_name = fullname  # store fullname properly
#             user.save()
#             messages.success(request, 'Account created successfully!')
#             return redirect('login_user')

    # ✅ Only render the registration page if GET or validation failed
    # return render(request, 'register.html')
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Signup
from .models import UploadFile
from .forms import ResumeForm
from django.http import FileResponse

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        country = request.POST.get("country")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")

        Signup.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            confirm_password=confirm_password,
            country=country
        )

        messages.success(request, "Account created successfully!")
        return redirect("signin")

    return render(request, "signup1.html")


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
from .models import Signup

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Signup.objects.get(email=email, password=password)
            messages.success(request, "Login successful!")
            return redirect("home")   # change this to your page
        except Signup.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("signin")

    return render(request, "login.html")


def home(request):
    return render(request,'home.html')         

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImgUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('image_list')
#     else:
#         form = ImgUploadForm()
#     return render(request, 'upload_image.html', {'form': form})

# def image_list(request):
#     images = ImgUpload.objects.all()
#     return render(request, 'image_list.html', {'images': images})

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



