from django.shortcuts import render
from report.models import City
from .forms import CityForm
import urllib2
import re
import json


# Create your views here.

def home(request):
	form=CityForm

	if request.method=='POST':
		print "inside if"
		form=CityForm(request.POST)
		if form.is_valid():
			form.save()
		city=City.objects.values()
		print "1"
		response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + str(city['city']) + '&appid=4a87519db6e540f39c6651e9e9f89a8b')
		print "2"
		data=json.load(response)
		print "3"
		temp = str(data['main']['temp']-273) + "C"
		print  "4"

		return render(request, "display.html", {'city':form, 'temp':temp})

	return render(request, "home.html")