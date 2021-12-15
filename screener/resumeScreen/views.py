from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import logging
import pandas as pd
from django.http import HttpResponse, Http404

from .models import  UploadResume
from resumeScreen.forms import UserSignupForm,UploadDes
from .resume_screening import resume_screen

# Landing page
def index(request):

	showAll= UploadResume.objects.filter(name=request.user)
	output=None
	form1 = UploadDes()
	# form2 = UploadRes()
	if request.method == "POST":
		
		form1 = UploadDes(request.POST, request.FILES)
		#skills=form1.cleaned_data['job_des_skills']
		#degree=form1.cleaned_data['job_des_degree']
		#skills = list(skills.split(" "))
		#degree = list(degree.split(" "))
		#output=shortlist(skills,degree)


		if form1.is_valid():
			
				skills=form1.cleaned_data['job_des_skills']
				degree=form1.cleaned_data['job_des_degree']
				#if skills!='' & degree!='':
				skills = list(skills.split(" "))
				degree = list(degree.split(" "))
				output=shortlist(skills,degree)
				des = form1.save(commit=False)
				des.name = request.user
				des.save()
			
				#if skills!='' & degree!='':
				return render(request,"output.html",{'output':output})
				#else:
				#	return redirect('index')


		else:
			form1 = UploadDes()
			#form2 = uploadRes(prefix = "form2")
	context_dict = {
		'form1' : form1,
		'output':output,
		}
	return render(request,"index.html",context_dict)

def output(request):
	return render(request,'output.html')

def user_registration(request):
	if request.method == 'POST':
		form=UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
		
		messages.success(request,"Account Created Successfully")
		print(request.FILES.getlist("file"))
		return redirect('index')
		
	else:
		form = UserSignupForm()
	
	return render(request,'registration/signup.html',{'form':form})
'''
def shortlist(skills,degree):
	req=[]
	req=skills+degree
	print("req",req)
	df=resume_screen()
	for i in req:
				drop_A=df.index[df[i] == 0.0]
				df.drop(df.index[drop_A],inplace=True)
	print("df",df)
	shortlisted=list(df['Candidate Name'])
	print(shortlisted)
	#shortlisted = df.to_html()
	#return HttpResponse(shortlisted)
	return shortlisted
'''
def shortlist(skills,degree):
	req=[]
	req=skills+degree
	print("req",req)
	df=resume_screen()
	for i in req:
				df[df[i] == 0.0]=None
	df=df.dropna()
	print(df)
	shortlisted=list(df['Candidate Name'])
	print(shortlisted)
	return shortlisted
