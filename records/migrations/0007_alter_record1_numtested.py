# Generated by Django 3.2.5 on 2021-07-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_alter_record1_numtested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record1',
            name='numtested',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
