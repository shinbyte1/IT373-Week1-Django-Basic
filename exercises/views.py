from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {
        'course': 'IT 373 - Web Systems and Technologies',
        'week1': 1,
    }
    return render(request, 'exercises/home.html', ctx)

def about(request):
    return render(request, 'exercises/about.html')