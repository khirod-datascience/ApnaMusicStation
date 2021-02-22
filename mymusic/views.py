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
    return render(request,'index1.html',out1)


def video(request):
        if request.method == 'POST':
                url = request.POST['URL']
                url=url.replace('watch?v=','embed/')
                print(url)
                out={'url':url}
                return render(request,'video.html',out) 
        return render(request,'video.html') 






