# Generated by Django 2.2.2 on 2019-06-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190613_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calories',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='fat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='salt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sugar',
            field=models.FloatField(default=0),
        ),
    ]
