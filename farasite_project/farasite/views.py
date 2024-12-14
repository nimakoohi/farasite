from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def services_view(request):
    return render(request, 'services.html')

def news_view(request):
    return render(request, 'news.html')

def contact_view(request):
    return render(request, 'contact.html')