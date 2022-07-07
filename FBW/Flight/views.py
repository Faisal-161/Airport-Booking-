from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight


def Home(request):

    #context = {
            #'Flight':Flight.objects.filter('departure', 'destination','departure_datetime','arrival_datetime'),
            
    #}
    return render(request ,"home.html")


def search_result(request):

    context ={

        'Flight': Flight.objects.filter('departure','destination')
    }
    return render(request, "search.html", context)


def Details(request):

    context ={

        'Flight': Flight
    }
    return render (request , "flight_details.html", context)
# Create your views here
