from django.shortcuts import render

def index(request):
	data = {'mydata': "Hello World! from my blog!"}
	return render(request, 'blog/index.html', data)