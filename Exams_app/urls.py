from Exams_app.views import index,main_page
from django.urls import path
urlpatterns = [
    path('my_page', index),
    path("my_html",main_page)
]