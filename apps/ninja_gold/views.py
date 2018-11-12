from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	context = {
		"somekey":"somevalue"
	}
	return render(request,'ninja_gold/index.html', context)