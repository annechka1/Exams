from Exams_app.models import Exams
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
import requests
from Exams_app.models import Teachers


def index(request):
    lesson=" "
    for x in Exams.objects.all():
        lesson=lesson+x.number_of_class+" "+x.surname+" "+x.subject+" "
    return HttpResponse(lesson)

def main_page(request):
    """if request.user is not None and request.user.has_perm('Exams_app.view_marks_exams'):
        print("Look,please")
    else:
        print("No?Why do you want to do?")"""
    return render(request, 'index.html')

def second_page(request):
    return render(request,'the_second_page.html')

def third_page(request):
    return render(request,'the_third.html')

def login_user(request):
    user= authenticate(
        username = request.POST["username"],
        password = request.POST["password"],
    )
    if user is None:
        return render(request,"the_second_page.html",{})
    else:
        login(request,user)
        return (HttpResponseRedirect("/my_html"))
def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return (HttpResponseRedirect("/my_html"))
    else:
        return HttpResponse("Not login")

def third_page(request):
    user = User.objects.create_user(
        request.POST["username"],
        password=request.POST["password"],
    )
    return HttpResponseRedirect("/my_html")

def new_register(request):
    return render(request, 'the_third.html')

def contacts_of_us(request):
    return render(request, 'contacts.html')
    # Create your views here.

def ajax_path(request):
    response={
        "message": "Hello"
    }
    return JsonResponse(response)

def ajax_path_2(request):
    users = User.objects.filter(username=request.POST["login"])
    if len(users) != 0 :
        response={
        "exist": 1
    }
    else:
        response = {
            "exist":0
        }
    return JsonResponse(response)





#def ajax_path_reg(request):
    #response={
        #"message": "User is succesfull create"
    #}
   # return JsonResponse(response)


"""import random
from datetime import datetime
from Exams_app.models import Marks_exams"""
from Exams_app.models import Marks_exams,Teachers
def experiment(request):
    size = 100000
    slice_size = 500
    Marks_exams.objects.all().delete()
    for x in range(int(size/slice_size)):
        slice=[]
        for x in range(slice_size):
            slice.append(
                Marks_exams(
                    history = str(random.randint(1,1000)),
                    english = str(random.randint(1, 1000)),
                    russian = str(random.randint(1, 1000))
                )
            )
        Marks_exams.objects.bulk_create(slice,slice_size)
    return render(request, 'index.html',{})

""" sum=0
for x in range(100):
    start = datetime.now()
    list(Marks_exams.objects.filter(
        history = random.randint(1, 1000),
        english = random.randint(1, 1000),
        russian = random.randint(1, 1000)
        )
    )
    delta = (datetime.now() - start).total_seconds()
    sum = sum + delta
print("Execution time of 100 requests:" +
      str(sum) + "seconds")
return render(request, 'index.html')"""

"""def experiment(request):
ls=[]
for x in range(10000000):
    ls.append(random.randint(1,100))

start = datetime.now() #list
for x in range(1000):
    random.randint(1,100) in ls
print("Searched the list 100 times"+str((datetime.now()-start).total_seconds())+ "sec.")

hash = set(ls)
start = datetime.now() #set

for x in range(1000):
    random.randint(1,100) in hash
print("Searched the set 100 times" + str((datetime.now() - start).total_seconds()) + "sec.")
return render(request, 'index.html')"""
import random
from django.utils.translation import ugettext as _,activate
from django.conf import settings
def main (request):
    activate("pl")
    response=render(
        request,
        "index.html",
        {"title": _("Main page"),"cart":Teachers.objects.filter(id=3)[0]}
    )
    x=96
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME, "pl",
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    return response

import pickle
from pymemcache import Client


def main_2(request):
    client = Client(("localhost",11211))
    surname = client.get("surname")
    if surname is None:
        surname = []
        for marks in Marks_exams.objects.all():
            surname.append(marks.history)
        client.set(
            "surname",
            pickle.dumps(surname),
            expire=60
        )
    else:
        surname = pickle.loads(surname)
    return render(
        request,
        "index.html",
        {
            "surname":surname
        }
    )

def server(request):
    Teachers.objects.filter(
        id=request.POST["id"]
    ).update(
        surname_of_teacher=request.POST["surname_of_teacher"],
        years_old=int(request.POST["years_old"])
    )
    return JsonResponse({"Satus":"Ok"})