# Generated by Django 4.2.2 on 2023-07-01 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='static/img')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('short_description', models.TextField(blank=True, max_length=500, null=True)),
                ('features1', models.CharField(blank=True, max_length=250, null=True)),
                ('features2', models.CharField(blank=True, max_length=250, null=True)),
                ('features3', models.CharField(blank=True, max_length=250, null=True)),
                ('event_story', models.TextField(blank=True, max_length=750, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
    ]