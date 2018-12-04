from django.contrib import admin

from .models import Xəbərlər,Tərəfdaş,Layihə,Tədbir,Haqqimizda,Qutu
class xeber(admin.ModelAdmin):
    list_display= ('başliq','tarix')

class ter(admin.ModelAdmin):
    list_display= ('ad','email')

class lay(admin.ModelAdmin):
    list_display= ('ad','idareEden','bashlamaTarix','bitmeTarix')
class təd(admin.ModelAdmin):
    list_display= ('ad','idareEden','bashlamaTarix')

class qu(admin.ModelAdmin):
    list_display= ('ad',)

admin.site.register(Xəbərlər,xeber)
admin.site.register(Qutu,qu)
admin.site.register(Tədbir,təd)
admin.site.register(Tərəfdaş,ter)
admin.site.register(Haqqimizda)
admin.site.register(Layihə,lay)

# Register your models here.
