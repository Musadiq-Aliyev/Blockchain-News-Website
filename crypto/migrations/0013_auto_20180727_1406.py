# Generated by Django 2.0.7 on 2018-07-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0012_bgphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haqqimizda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('başliq', models.CharField(max_length=2000)),
                ('tarix', models.DateTimeField(verbose_name='Zaman')),
                ('mezmun', models.CharField(max_length=20000)),
                ('şəkil', models.ImageField(blank=True, upload_to='HaqqimizdaŞekil')),
            ],
        ),
        migrations.AlterField(
            model_name='bgphoto',
            name='shekil',
            field=models.ImageField(default='bg/cb.jpg', upload_to='bg/'),
        ),
    ]
