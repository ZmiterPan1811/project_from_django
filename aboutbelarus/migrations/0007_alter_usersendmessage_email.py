# Generated by Django 3.2.6 on 2021-09-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutbelarus', '0006_auto_20210920_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersendmessage',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Email'),
        ),
    ]
