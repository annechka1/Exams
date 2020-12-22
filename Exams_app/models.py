from django.db import models
class Exams(models.Model):
    number_of_class = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
#Exams.objects.filter(number_of_class="9A")
#Exams.objects.filter(subject="история").delete()
class Marks_exams(models.Model):
    history = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    russian = models.IntegerField(default=0)
class Teachers(models.Model):
    surname_of_teacher = models.CharField(max_length=100)
#Teachers.objects.filter(surname_of_teacher='Корнеева').update(surname_of_teacher='Филатов')
class Knowledge_level(models.Model):
    result_of_exams=models.CharField(max_length=100)
# Create your models here.
