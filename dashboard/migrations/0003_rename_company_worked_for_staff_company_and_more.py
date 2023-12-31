# Generated by Django 4.2.2 on 2023-06-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_staff_company_worked_for_staff_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='company_worked_for',
            new_name='company',
        ),
        migrations.AddField(
            model_name='staff',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
