# Generated by Django 3.2.5 on 2021-07-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_auto_20210719_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record1',
            name='avgratedeaths_last7',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
