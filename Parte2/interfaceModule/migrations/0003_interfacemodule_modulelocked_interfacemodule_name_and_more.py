# Generated by Django 4.1.2 on 2022-10-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceModule', '0002_remove_interfacemodule_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfacemodule',
            name='moduleLocked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interfacemodule',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interfacemodule',
            name='progression',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interfacemodule',
            name='quantityMicroModules',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interfacemodule',
            name='state',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
