from Exams_app.views import *
#from Exams_app.views import experiment
from django.urls import path
urlpatterns = [
    path('my_page', index),
    path("my_html",main),
    path("the_second_page",second_page),
    path("puth",login_user),
    path("new_logout",do_logout),
    path("the_third",third_page),
    path("register",new_register),
    path("contacts",contacts_of_us),
    path("ajax_path",ajax_path),
    path("cheak_login",ajax_path_2),
    #path("ajax_path_reg",ajax_path_reg),
    path("bd_index",experiment),
    path("teachers",server)
]