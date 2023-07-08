# Generated by Django 4.0 on 2022-02-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_husbandary', '0019_alter_animal_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='vaccinated',
        ),
        migrations.AddField(
            model_name='animal',
            name='vaccinated',
            field=models.ManyToManyField(to='animal_husbandary.vaccine'),
        ),
    ]