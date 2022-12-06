from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import mimetypes

# Create your views here.

def homePage(request):
  return render(request, 'srivats/home.html')


def workPage(request):
 
    

    work = Work.objects.all()
   

    
    
    context = {'work':work}
    return render(request, 'srivats/work.html', context)

def educationPage(request):
    education = Education.objects.all()



    return render(request, 'srivats/education.html', {'education':education})

def projectsPage(request):
    projects = Projects.objects.all()



    return render(request, 'srivats/projects.html',{'projects':projects})

def hobbiesPage(request):
    return render(request, 'srivats/hobbies.html')




def resumePage(request):
    fl_path = 'static/resources/Srivats\'s Resume.pdf'
    filename = 'Srivats\'s Resume.pdf'
    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    

