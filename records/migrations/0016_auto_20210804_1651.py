# Generated by Django 3.2.5 on 2021-08-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0015_alter_record1_avgratedeaths_last7'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record1',
            name='numactive',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numconf',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numdeaths',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numdeathstoday',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numprob',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtoday',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtotal',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='percentactive',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='percentdeath',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='percentoday',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='rateactive',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='ratedeaths',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='ratetotal',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
