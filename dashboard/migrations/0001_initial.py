# Generated by Django 4.2.2 on 2023-06-29 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_photo', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('about_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('admin', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
