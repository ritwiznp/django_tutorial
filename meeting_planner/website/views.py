from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))


def about(request):
    return HttpResponse("I'm Ritwiz")
