# Generated by Django 3.1.7 on 2021-03-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiledesa', '0002_auto_20210325_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparatur',
            name='slug',
            field=models.SlugField(max_length=225),
        ),
    ]
