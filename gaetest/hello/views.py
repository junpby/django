#-*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def greet(request):
	return render_to_response('base.html',{})
	#return HttpResponse("Hello World of Django!")
