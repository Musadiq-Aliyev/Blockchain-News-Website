# Generated by Django 2.0.7 on 2018-07-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0010_auto_20180727_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tədbir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200)),
                ('idareEden', models.CharField(max_length=200)),
                ('elaqeNomresi', models.CharField(max_length=200)),
                ('bashlamaTarix', models.DateTimeField(verbose_name='Başlayır')),
                ('shekil', models.ImageField(default='layihe/proj.png', upload_to='layihe/')),
                ('meqsed', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Tədbirlər',
            },
        ),
    ]
