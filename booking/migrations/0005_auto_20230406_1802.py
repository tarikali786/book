# Generated by Django 3.2.8 on 2023-04-06 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20230406_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]