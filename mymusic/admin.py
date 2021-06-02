from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(musiclist)
class musiclistAdmin(admin.ModelAdmin): 
    list_display = ('Title','Link') 

    
#admin.site.register(musiclist)



class aListMessage(admin.ModelAdmin):
    list_display = ('name','message', 'date','time')
 

admin.site.register(aMessages, aListMessage)


admin.site.register(aImages)