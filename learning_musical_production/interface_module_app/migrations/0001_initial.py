# Generated by Django 4.1.2 on 2022-10-24 18:39

from django.db import migrations, models
import django.forms.widgets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('answer', models.CharField(blank=True, max_length=5)),
                ('questions', models.CharField(blank=True, max_length=5)),
                ('qualification', models.DecimalField(blank=True, decimal_places=3, max_digits=5)),
                ('approval_date', models.DateField(auto_now_add=True)),
                ('number_attempts', models.IntegerField()),
            ],
            options={
                'verbose_name': 'interface_module_evaluation',
            },
        ),
        migrations.CreateModel(
            name='InterfaceModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('moduleLocked', models.BooleanField(verbose_name=True)),
                ('status', models.BooleanField()),
                ('progression', models.DecimalField(decimal_places=2, max_digits=4)),
                ('quantity_microModules', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'interface_module',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('psdw', models.CharField(max_length=15, verbose_name=django.forms.widgets.PasswordInput)),
                ('country', models.CharField(max_length=30)),
                ('date_birth', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('progression', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name': 'user_interface_module',
            },
        ),
    ]
