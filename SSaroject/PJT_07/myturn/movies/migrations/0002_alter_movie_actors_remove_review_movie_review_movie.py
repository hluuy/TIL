# Generated by Django 4.2.6 on 2023-10-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.actor'),
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ManyToManyField(to='movies.movie'),
        ),
    ]
