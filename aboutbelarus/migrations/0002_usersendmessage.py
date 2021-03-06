# Generated by Django 3.2.6 on 2021-09-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutbelarus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSendMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='E-mail')),
                ('message', models.TextField(blank=True, verbose_name='Сообщение пользователя')),
                ('time_sending', models.DateTimeField(auto_now_add=True, verbose_name='Время отправки сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['-time_sending', 'name'],
            },
        ),
    ]
