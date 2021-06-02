from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import *
import os
import random
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





# Create your views here.
@login_required(login_url='alogin')
def aindex(request):
    amessagelist=aMessages.objects.all()

    if request.method == 'POST':
        
        if request.POST.get('message'):
            post=aMessages()
            post.name=request.user
            post.message= request.POST.get('message')
            post.save()    
            return redirect('aindex')

        else:
            return redirect('aindex')

    aimagelist=aImages.objects.all()
    out={'amessagelist':amessagelist,
    'aimagelist':aimagelist,}
    return render(request,'aindex.html',out)

def aimage(request):
    if request.method == 'POST':
        myfile = request.FILES.get('file1')
        # fs = FileSystemStorage()
        # filename=fs.save(myfile.name, myfile)
        print(myfile)
        post=aImages()
        post.name=request.user
        post.image=request.FILES.get('file1',)
        post.save()
        return redirect('aindex')

   
    return render(request,'index.html')
    # imagelist=Images.objects.all()
    # # files=[]
    # # dir='media'
    # # for filename in os.listdir(dir):
    # #     f = os.path.join(dir, filename)
    # #     # checking if it is a file
    # #     if os.path.isfile(f):
    # #         files.append(f)
    # out={'imagelist':imagelist,}
    # return redirect('index',out)


def aloginPage(request):
    if request.user.is_authenticated:
        return redirect('aindex')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('aindex')
            else:
                messages.info(request, 'Username OR password is incorrect')

     
        return render(request, 'Login.html',)




def logoutUser(request):
	logout(request)
	return redirect('login')










