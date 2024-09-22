# Generated by Django 5.1 on 2024-09-03 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_module_app', '0010_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcion',
            name='es_correcta',
            field=models.BooleanField(default=False, verbose_name='¿Esta es la pregunta correcta?'),
        ),
        migrations.AlterField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='interface_module_app.pregunta'),
        ),
        migrations.AlterField(
            model_name='opcion',
            name='texto',
            field=models.TextField(verbose_name='Introduce una opción de respuesta'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='texto',
            field=models.TextField(verbose_name='Introduce pregunta'),
        ),
    ]
