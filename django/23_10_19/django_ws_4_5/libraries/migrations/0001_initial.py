# Generated by Django 4.2.2 on 2023-10-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.TextField()),
                ('pubdate', models.DateField(blank=True, null=True)),
                ('pricesales', models.IntegerField(null=True)),
                ('pricestandard', models.IntegerField(null=True)),
                ('publisher', models.CharField(max_length=50)),
                ('adult', models.BooleanField(default=False)),
            ],
        ),
    ]
