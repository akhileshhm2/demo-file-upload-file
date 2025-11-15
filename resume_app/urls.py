from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("", views.home, name="home"),  
    path("report/",views.report,name='report'),
    # path("upload/",views.upload,name='upload'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name="contact"),
    path("upload2/",views.upload2,name='upload2'),
    path('view/<int:file_id>/', views.view_file, name='view_file'),
]
