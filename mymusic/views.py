from django.shortcuts import render
import random
from .models import musiclist
# Create your vi
# ews here.
def index(request):
    
    songs=musiclist.objects.all()
    #print(songs)
    p=len(songs)
    products=list(musiclist.objects.all())
    products = random.sample(products, p)

    out1={'songs':songs,
            'products':products}
    return render(request,'index.html',out1)






