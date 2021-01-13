from Exams_app.models import Exams
from django.http import HttpResponse
def index(request):
    lesson=" "
    for x in Exams.objects.all():
        lesson=lesson+x.number_of_class+" "+x.surname+" "+x.subject+" "
    return HttpResponse(lesson)
from django.shortcuts import render
def main_page(request):
    context={
        "header":"Menu"
    }
    return render(request, 'index.html', context)
# Create your views here.
