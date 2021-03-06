# Generated by Django 2.0.7 on 2018-08-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0018_auto_20180807_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tərəfdaş',
            name='nomre',
        ),
        migrations.RemoveField(
            model_name='tərəfdaş',
            name='soyad',
        ),
        migrations.AddField(
            model_name='tərəfdaş',
            name='url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='layihə',
            name='shekil',
            field=models.ImageField(default='Layihə/proj.png', upload_to='Layihə/'),
        ),
        migrations.AlterField(
            model_name='tədbir',
            name='shekil',
            field=models.ImageField(default='Tədbir/proj.png', upload_to='Tədbir/'),
        ),
        migrations.AlterField(
            model_name='tərəfdaş',
            name='shekil',
            field=models.ImageField(default='Tərəfdaş/user.png', upload_to='Tərəfdaş/'),
        ),
        migrations.AlterField(
            model_name='xəbərlər',
            name='shekil',
            field=models.ImageField(default='Xəbərlər/qazet.jpg', upload_to='Xəbərlər/'),
        ),
        migrations.AlterField(
            model_name='əlaqə',
            name='shekil',
            field=models.FileField(default='Əlaqə/cb.jpg', upload_to='Əlaqə/'),
        ),
    ]
