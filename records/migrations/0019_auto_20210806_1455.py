# Generated by Django 3.2.5 on 2021-08-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0018_auto_20210806_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record1',
            name='numconf',
            field=models.CharField(blank=True, max_length=255, verbose_name='Number_of_confirmed'),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numdeaths',
            field=models.CharField(blank=True, max_length=255, verbose_name='Number_of_deaths'),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numrecover',
            field=models.CharField(blank=True, max_length=255, verbose_name='Number_of_recovered'),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtested',
            field=models.CharField(blank=True, max_length=255, verbose_name='Number_of_tested'),
        ),
        migrations.AlterField(
            model_name='record1',
            name='prnameFR',
            field=models.CharField(max_length=200, verbose_name='Province_French_Name'),
        ),
    ]
