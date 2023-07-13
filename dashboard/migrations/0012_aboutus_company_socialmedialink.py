# Generated by Django 4.2.2 on 2023-07-01 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_contacts_options_alter_events_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('short_description', models.TextField(blank=True, max_length=300, null=True)),
                ('vision', models.CharField(blank=True, max_length=150, null=True)),
                ('mission', models.CharField(blank=True, max_length=150, null=True)),
                ('values', models.CharField(blank=True, max_length=150, null=True)),
                ('closing_description', models.TextField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('tagline', models.CharField(blank=True, max_length=300, null=True)),
                ('call1', models.CharField(blank=True, max_length=16, null=True)),
                ('call', models.CharField(blank=True, max_length=16, null=True)),
                ('email1', models.EmailField(blank=True, max_length=254, null=True)),
                ('opening_time', models.CharField(blank=True, max_length=40, null=True)),
                ('closing_time', models.CharField(blank=True, max_length=40, null=True)),
                ('first_day', models.CharField(blank=True, max_length=40, null=True)),
                ('last_day', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('county', models.CharField(blank=True, max_length=40, null=True)),
                ('location', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
    ]
