from django.contrib import admin

# Register your models here.
from .models import musiclist 

@admin.register(musiclist)
class musiclistAdmin(admin.ModelAdmin): 
    list_display = ('Title','Link') 

    
#admin.site.register(musiclist)