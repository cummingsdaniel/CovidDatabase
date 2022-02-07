# Generated by Django 3.2.5 on 2021-07-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_alter_record1_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record1',
            name='numconf',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numdeaths',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numprob',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numrecover',
            field=models.IntegerField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtested',
            field=models.IntegerField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='numtoday',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='prname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='prnameFR',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record1',
            name='pruid',
            field=models.IntegerField(max_length=255),
        ),
    ]
