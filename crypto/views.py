from crypto.models import Xəbərlər,Tərəfdaş,Layihə,Tədbir,Haqqimizda,Qutu
from django.core.mail import send_mail, BadHeaderError,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import get_template



def anasəhifə(request):

    #qiymetler
	data=Qutu.objects.filter(ad='a_vidyo')

	pho=Qutu.objects.filter(ad='a_shekil')
	return render(request,'anasəhifə.html', {'data':data,'pho':pho})



k=6
def xəbərlər(request):
	xəbərdata=Xəbərlər.objects.order_by('-tarix')[:k]

	seyf=(len(xəbərdata)+k-1)//k
	sayfa=[]
	for i in range(0,seyf):
		sayfa.append(i+1)
	xəbərdata=xəbərdata[0:k]
	try:
		import requests
		import json
		api_request= requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
		api=json.loads(api_request.content)
	except:
		api=''
	if(len(sayfa)==1):
		sayfa=[]
	return render(request,'xəbərlər.html', {'api':api,'xəbərdata':xəbərdata,'sayfa':sayfa })
def tədbirlər_xəbərlər(request):

	xəbərdata=[]
	xəbərdata=Xəbərlər.objects.all().exclude(tedbir='').order_by('-tarix')
	seyf=(len(xəbərdata)+k-1)//k
	sayfa=[]

	for i in range(0,seyf):
		sayfa.append(i+1)

	xəbərdata=xəbərdata[0:k]
	try:
		import requests
		import json
		api_request= requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
		api=json.loads(api_request.content)
	except:
		api=''
	if(len(sayfa)==1):
		sayfa=[]
	return render(request,'xəbərlər.html', {'api':api,'xəbərdata':xəbərdata,'sayfa':sayfa })

def xəbərs(request,seyfe):
	xəbərdata=Xəbərlər.objects.all()
	seyf=(len(xəbərdata)+k-1)//k
	sayfa=[]
	for i in range(0,seyf):
		sayfa.append(i+1)
	xəbərdata=xəbərdata[(seyfe-1)*k:seyfe*k]
	if(len(xəbərdata)<1):
		return redirect('/xəbərlər')#xəbərlər(request)
	try:
		import requests
		import json
		api_request= requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
		api=json.loads(api_request.content)
	except:
		api=''
	return render(request,'xəbərlər.html', {'api':api,'xəbərdata':xəbərdata,'sayfa':sayfa })

def xəbər(request,mezmun):

    import requests
    import json

    data=Xəbərlər.objects.filter(başliq=mezmun)

    # xeberler

    return render(request,'xəbər.html', {'data':data ,'test':mezmun})

def layihə(request,mezmun):

    import requests
    import json

    data=Layihə.objects.filter(ad=mezmun)

    # xeberler

    return render(request,'layihə.html', {'data':data ,'test':mezmun})


def s(request):


	if request.method=='POST':
		import requests
		import json

		quote =request.POST['quote']
		quote=quote.upper()
		xəbərdata=Xəbərlər.objects.all().filter(başliq__contains=quote)
		layihədata=Layihə.objects.all().filter(ad__contains=quote)


		return render(request,'s.html',{'xəbərdata':xəbərdata,'quote':quote,'layihədata':layihədata})

	else:
		notfound = "Zəhmət olmasa  axtariş edin..."
		return render(request,'s.html', {'notfound': notfound})

def tədbirlər(request):
    tədbirdata=Tədbir.objects.all()
    return render(request,'tədbirlər.html', {'tədbirdata':tədbirdata})

def tərəfdaşlar(request):
    tərəfdaşdata=Tərəfdaş.objects.all()
    return render(request,'tərəfdaşlar.html', {'tərəfdaşdata':tərəfdaşdata})

def layihələr(request):
	layihədata=Layihə.objects.all()
	return render(request,'layihələr.html', {'layihədata':layihədata})

def əlaqə(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            Ad= request.POST.get(
                'Ad'
            , '')
            Email = request.POST.get(
                'Email'
            , '')
            form_content = request.POST.get('İsmaric', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')

            context = {
                'Ad': Ad,
                'Email': Email,
                'form_content': form_content,
            }
            İsmaric = template.render(context)

            email = EmailMessage(
                "Sizin Yeni İsmariciniz var",
                İsmaric,
                "Your website" +'',
                ['musadiq.aliyev@gmail.com'],
                headers = {'Reply-To': Email }
            )
            email.send()
            return redirect('əlaqə')

    return render(request, 'əlaqə.html', {
        'form': form_class,
    })


def haqqimizda(request):
    	Haqqimizdadata=Haqqimizda.objects.all()
    	return render(request,'haqqimizda.html', {'Haqqimizdadata':Haqqimizdadata})
