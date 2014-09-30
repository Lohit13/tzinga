from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from hackv5.models import Byld
from django.core.urlresolvers import reverse
from django import forms
from models import *

import csv
from django.utils.encoding import smart_str
import os.path
direct = os.path.dirname(__file__)
print direct
ab = os.path.join(direct, '/static/hackv5/acdef.csv')
abm = os.path.join(direct, '/static/hackv5/acdefm.csv')
    
def index(request):
    #template = loader.get_template('hackv5/index.html')
    #return HttpResponse("Hello, world. You're at the poll index.")
	print request.method
	if request.method == 'POST':
		newdoc = Byld(field1=request.POST.get('firstname1'),field2=request.POST.get('firstname2'),field3=request.POST.get('firstname3'))
		newdoc.save()
		file = open(ab, "w")
	    	for obj in Byld.objects.all():
			file.write(obj.field1+","+obj.field2+","+obj.field3+"\n")
		file.close()
		return HttpResponseRedirect(reverse('index'))
 	else:
		# A empty, unbound form
		# Load documents for the list page
		documents = Byld.objects.all()
		# Render list page with the documents and the form
		return render_to_response('index.html',{'documents': documents},context_instance=RequestContext(request))

def attendence(request):
    #template = loader.get_template('hackv5/index.html')
    #return HttpResponse("Hello, world. You're at the poll index.")
	print request.method
	if request.method == 'POST':
		newdoc = Byld(field1=request.POST.get('firstname1'),field2=request.POST.get('firstname2'),field3=request.POST.get('firstname3'))
		newdoc.save()
		file = open(ab, "w")
		print ":ojvknsvknsonv"
	    	for obj in Byld.objects.all():
			file.write(obj.field1+","+obj.field2+","+obj.field3+"\n")
		file.close()
		return HttpResponseRedirect(reverse('attendence'))
 	else:
		# A empty, unbound form
		# Load documents for the list page
		documents = Byld.objects.all()
		# Render list page with the documents and the form
		return render_to_response('attendence.html',{'documents': documents},context_instance=RequestContext(request))


def mess(request):
    #template = loader.get_template('hackv5/index.html')
    #return HttpResponse("Hello, world. You're at the poll index.")
	print request.method
	if request.method == 'POST':
		newdoc = Byldmess(field11=request.POST.get('firstname1'),field21=request.POST.get('firstname2'),field31=request.POST.get('firstname3'))
		newdoc.save()
		file = open(abm, "w")
		print ":ojvknsvknsonv"
	    	for obj in Byldmess.objects.all():
			file.write(obj.field11+","+obj.field21+","+obj.field31+"\n")
		file.close()
		return HttpResponseRedirect(reverse('mess'))
 	else:
		# A empty, unbound form
		# Load documents for the list page
		documents = Byldmess.objects.all()
		# Render list page with the documents and the form
		return render_to_response('mess.html',{'documents': documents},context_instance=RequestContext(request))
   
