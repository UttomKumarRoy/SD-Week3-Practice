import datetime
from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'name':"uttom kumar roy",
        'age':28,
        'players':['Sakib','Masrafee', 'Liton'],
        'date': datetime.datetime.now(),
            'list1': [
                {'name': 'Josh', 'age': 19},
                {'name': 'Dave', 'age': 22},
                {'name': 'Joe', 'age': 31},
            ]
    }
    return render(request, 'home.html',context)
