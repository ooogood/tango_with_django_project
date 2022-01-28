from django.shortcuts import render

from django.http import HttpResponse

def index(request):
# chapter 3
	# return HttpResponse('Rango says hey there partner!<br><a href=\'/rango/about/\'>About</a>')
# chapter 4
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
# chapter 3
	# return HttpResponse('Rango says here is the about page.<br><a href=\'/rango/\'>Index</a>')
# chapter 4
	context_dict = {'myname': '2669729C'}
	return render(request, 'rango/about.html', context=context_dict)