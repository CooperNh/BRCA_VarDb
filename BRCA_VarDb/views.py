from django.http import HttpResponse
from .models import Patient
from django.shortcuts import render
from django.template import loader

def index(request):
	data = Patient.objects.all()
	#print (data)
	return render_to_response("patients.html", {'data', data})

