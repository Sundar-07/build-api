# Generated by Django 3.1.6 on 2021-04-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectform',
            name='suit',
        ),
    ]
