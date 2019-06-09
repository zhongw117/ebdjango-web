from django.shortcuts import render


def index(request):

	return render(request, "index.html", {})

def workexperience(request):

	return render(request, "workexperience.html", {})

def externallink(request):

	return render(request, "externallink.html", {})