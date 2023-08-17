# Generated by Django 4.2.4 on 2023-08-17 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=25, verbose_name='Букет')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='flowers_img', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Букет',
                'verbose_name_plural': 'Букеты',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(db_index=True, max_length=50, verbose_name='Telegram id')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Номер телефона')),
                ('adress', models.CharField(blank=True, max_length=50, null=True, verbose_name='Адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Событие')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(verbose_name='Дата доставки')),
                ('delivery_time', models.CharField(choices=[('AM', '11:00 - 15:00'), ('PM', '15:00 - 20:00')], default='PM', max_length=20, verbose_name='Время доставки')),
                ('bouquet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bot.catalog', verbose_name='Букет')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_order_set', to='bot.client', verbose_name='Клиент')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier_order_set', to='bot.client', verbose_name='Курьер')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_consultation_set', to='bot.client', verbose_name='Клиент')),
                ('florist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='florist_consultation_set', to='bot.client', verbose_name='Флорист')),
            ],
            options={
                'verbose_name': 'Консультацию',
                'verbose_name_plural': 'Консультации',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='event',
            field=models.ManyToManyField(to='bot.event'),
        ),
    ]
