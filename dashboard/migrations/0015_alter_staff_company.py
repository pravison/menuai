# Generated by Django 4.2.2 on 2023-07-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_rename_call_company_call2_company_email2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='company',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
