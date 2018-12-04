import datetime
from django.db import models
from django.utils import timezone

class Xəbərlər(models.Model):
    class Meta:
        verbose_name_plural = "Xəbərlər"
    başliq=models.CharField(max_length=2000,primary_key=True)
    shekil=models.ImageField(upload_to = 'Xəbərlər/', default = 'Xəbərlər/qazet.jpg')
    tarix=models.DateTimeField('Tarix')
    muellif=models.CharField(max_length=2000,blank=True)
    mezmun=models.TextField()
    tedbir=models.CharField(max_length=2000,blank=True)
    tedbir_Link=models.CharField(max_length=2000,blank=True)

class Tərəfdaş(models.Model):
    class Meta:
        verbose_name_plural = "Tərəfdaşlar"
    ad=models.CharField(max_length=200)

    email=models.EmailField(primary_key=True)
    shekil=models.ImageField(upload_to = 'Tərəfdaş/', default = 'Tərəfdaş/user.png')
    url = models.URLField(null=True, blank=True, default='')
class Layihə(models.Model):
    class Meta:
        verbose_name_plural = "Layihələr"
    ad=models.CharField(max_length=200)
    idareEden=models.CharField(max_length=200)
    elaqeNomresi=models.CharField(max_length=200)
    bashlamaTarix=models.DateTimeField('Başlayır')
    bitmeTarix=models.DateTimeField('Bitir')
    shekil=models.ImageField(upload_to = 'Layihə/', default = 'Layihə/proj.png')
    meqsed=models.TextField()
class Tədbir(models.Model):
    class Meta:
        verbose_name_plural = "Tədbirlər"
    ad=models.CharField(max_length=200)
    idareEden=models.CharField(max_length=200)
    elaqeNomresi=models.CharField(max_length=200)
    bashlamaTarix=models.DateTimeField('Başlayır')
    shekil=models.ImageField(upload_to = 'Tədbir/', default = 'Tədbir/proj.png')
    meqsed=models.TextField()
class Haqqimizda(models.Model):
    class Meta:
        verbose_name_plural = "Haqqımızda"
    başliq=models.CharField(max_length=2000)
    tarix=models.DateTimeField('Zaman')
    mezmun=models.CharField(max_length=20000)
    shekil=models.ImageField(upload_to='HaqqimizdaŞekil/', blank=True)
class Qutu(models.Model):
    class Meta:
        verbose_name_plural = "Qutu"
        verbose_name_plural = "Qutular"
    ad=models.CharField(max_length=200)
    shekil=models.FileField(upload_to = 'Qutu/', default = 'Qutu/cb.jpg')
