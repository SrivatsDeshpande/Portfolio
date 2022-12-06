from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('work/', views.workPage, name='work' ),
    path('education/', views.educationPage, name='education' ),
    path('projects/', views.projectsPage, name='projects' ),
    path('hobbies/', views.hobbiesPage, name='hobbies' ), 
    path('resume/', views.resumePage, name='resume' )
]