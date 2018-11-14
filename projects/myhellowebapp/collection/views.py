from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
# this is your new view

    number = 7

    thing = "Alam Aara"

    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
        })
