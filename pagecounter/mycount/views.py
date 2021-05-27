from django.shortcuts import render

# Create your views here.
def home(request):
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    return render(request, 'home.html', {'c':newcount})# it is usefull when we want to accesss info tht how much time user visit in in that session