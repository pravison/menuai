# Generated by Django 4.2.2 on 2023-06-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_contacts_options_contacts_replied'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=16)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=10)),
                ('number', models.IntegerField()),
                ('message', models.TextField(max_length=400)),
                ('send_at', models.DateTimeField(auto_now_add=True)),
                ('attended', models.BooleanField(default=False)),
            ],
        ),
    ]
