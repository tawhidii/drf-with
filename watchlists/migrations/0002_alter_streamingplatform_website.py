# Generated by Django 3.2 on 2022-05-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamingplatform',
            name='website',
            field=models.URLField(max_length=100),
        ),
    ]
