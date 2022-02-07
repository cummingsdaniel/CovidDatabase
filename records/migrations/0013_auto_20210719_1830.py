# Generated by Django 3.2.5 on 2021-07-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_alter_record1_numtested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record1',
            name='avgdeaths_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='avgincidence_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='avgratedeaths_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='avgtotal_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numdeaths_last14',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numdeaths_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numrecover',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numrecoveredtoday',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtestedtoday',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtotal_last14',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtotal_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='percentrecover',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='ratedeaths_last14',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='ratedeaths_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='ratetested',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='ratetotal_last14',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='ratetotal_last7',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
