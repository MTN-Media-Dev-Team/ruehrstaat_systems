# Generated by Django 4.0.5 on 2023-01-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0004_alter_carrier_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='previousLocation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
