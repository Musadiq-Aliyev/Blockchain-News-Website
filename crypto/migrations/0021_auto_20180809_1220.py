# Generated by Django 2.0.7 on 2018-08-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0020_auto_20180809_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qutu',
            options={'verbose_name_plural': 'Qutular'},
        ),
        migrations.AlterField(
            model_name='qutu',
            name='shekil',
            field=models.FileField(default='Qutu/cb.jpg', upload_to='Qutu/'),
        ),
    ]