# Generated by Django 3.2.6 on 2021-09-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutbelarus', '0003_auto_20210919_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersendmessage',
            name='message',
            field=models.TextField(blank=True, verbose_name='Сообщение'),
        ),
    ]
