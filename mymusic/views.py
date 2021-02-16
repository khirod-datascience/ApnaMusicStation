from django.shortcuts import render
import random
from .models import musiclist
# Create your vi
# ews here.
def index(request):
    
    songs=musiclist.objects.all()
    print(songs)
    p=len(songs)
    products=list(musiclist.objects.all())
    products = random.sample(products, p)
    songlist={}
    #for song in products:
        # songlist['Title']=song.Title
        # songlist['Link']=song.Link
        # songlist['Desc']=song.Desc
        # songlist.append(song.Link)
        # songlist.append(song.Title)
        #print(song.Title)
        #print(song)
        #print(dir(song))
    #random.shuffle(songlist)
    # print(songlist)
    # instance = vlc.Instance()
    # player = instance.media_player_new()
    # my_list = fl
    # for song in fl:
    #     if flag1 == "start":
    #         player.set_mrl(song)
    #         #player = vlc.MediaPlayer(song)
    #         player.play()
    #     if flag1 == "stop":
    #         player.pause()
    
    out1={'songs':songs,
            'songlist':songlist,
            'products':products}
    return render(request,'index.html',out1)






