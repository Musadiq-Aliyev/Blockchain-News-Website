from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.anasəhifə,name="anasəhifə"),
     path('xəbərlər/', views.xəbərlər,name="xəbərlər"),
    path('xəbərlər/seyfe/<int:seyfe>', views.xəbərs,name="xəbər"),
    path('xəbərlər/<str:mezmun>/', views.xəbər,name="xəbər"),

    path('s/', views.s,name="s"),
	path('tədbirlər/', views.tədbirlər,name="tədbirlər"),
	path('tədbirlər/xəbərlər', views.tədbirlər_xəbərlər,name="tədbirlər_xəbərlər"),
	path('tərəfdaşlar/', views.tərəfdaşlar,name="tərəfdaşlar"),
	path('layihələr/', views.layihələr,name="layihələr"),
	 path('layihələr/<str:mezmun>/', views.layihə,name="layihələr"),
	path('haqqimizda/', views.haqqimizda,name="haqqimizda"),
	path('əlaqə/', views.əlaqə,name="əlaqə"),


]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
