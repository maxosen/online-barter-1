# Generated by Django 3.1 on 2021-01-01 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20210101_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='listed_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]