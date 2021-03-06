# Generated by Django 3.1.6 on 2021-04-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.IntegerField(choices=[(1, 'Diamond'), (2, 'Spade'), (3, 'Heart'), (4, 'Club')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(default='', max_length=100)),
                ('project_name', models.CharField(default='paradise', max_length=150)),
                ('tower', models.CharField(default='A', max_length=50)),
                ('floor', models.IntegerField(default='1', max_length=30)),
                ('unit_status', models.IntegerField(default='0', max_length=10)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
