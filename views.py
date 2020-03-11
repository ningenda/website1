from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc='City that never sleeps'
    dest1.price=700

    dest2=Destination()
    dest2.name='patna'
    dest2.desc='City that never sleeps'
    dest2.price=700

    dest3=Destination()
    dest3.name='ranchi'
    dest3.desc='City that never sleeps'
    dest3.price=700

    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})
