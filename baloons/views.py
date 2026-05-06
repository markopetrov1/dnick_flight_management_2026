from django.shortcuts import render, redirect, get_object_or_404

from baloons.forms import FlightForm
from baloons.models import Flight


def homepage(request):
    flights = Flight.objects.all()

    data = {
        'flights': flights
    }

    return render(request, "homepage.html", context=data)


def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)

        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.save()
        return redirect('homepage')
    else:
        form = FlightForm()
        data = {
            'form': form
        }
        return render(request, 'add-flight.html', context=data)



def get_details(request, id):
    # flight = Flight.objects.filter(id=id).first()

    flight = get_object_or_404(Flight, id=id)
    data = {
        'flight': flight
    }
    return render(request, 'details.html', data)