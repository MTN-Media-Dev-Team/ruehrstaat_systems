# Generated by Django 4.0.5 on 2023-01-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0007_alter_carrier_dockingaccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrierservice',
            name='label',
            field=models.CharField(default='Empty', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrierservice',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
