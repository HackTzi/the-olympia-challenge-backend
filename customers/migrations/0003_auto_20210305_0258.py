# Generated by Django 3.1.7 on 2021-03-05 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_notification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
    ]