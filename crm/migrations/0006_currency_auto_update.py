# Generated by Django 5.1.4 on 2024-12-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_company_owner_alter_contact_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='auto_update',
            field=models.BooleanField(default=True, verbose_name='This currency is subject to automatic updating.'),
        ),
    ]