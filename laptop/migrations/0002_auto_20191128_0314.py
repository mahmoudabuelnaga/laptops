# Generated by Django 2.2.7 on 2019-11-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inher',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
