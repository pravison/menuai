# Generated by Django 4.2.2 on 2023-07-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_aboutus_image_alter_company_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='on_shift',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='waiter',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]