# Generated by Django 3.2.5 on 2021-07-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_auto_20210719_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record1',
            name='update',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
