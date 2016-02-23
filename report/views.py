from django.shortcuts import render
from report.models import City
from .forms import CityForm
import urllib2
import re
import json


# Create your views here.

def home(request):
	form=CityForm()

	if request.method=='POST':
		form=CityForm(request.POST)
		if form.is_valid():
			form.save()
		try:
			city=list(City.objects.values())
			response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + str(city[-1]['city']) + '&appid=4a87519db6e540f39c6651e9e9f89a8b')
			data=json.load(response)
			temp = str(data['main']['temp']-273) + "C"

		except City.DoesNotExist:
			pass

		return render(request, "display.html", {'city':form, 'temp':temp})

	return render(request, "home.html")

	