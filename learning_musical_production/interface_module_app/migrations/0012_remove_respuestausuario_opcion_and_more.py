# Generated by Django 5.1 on 2024-09-04 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface_module_app', '0011_alter_opcion_es_correcta_alter_opcion_pregunta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestausuario',
            name='opcion',
        ),
        migrations.RemoveField(
            model_name='respuestausuario',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='respuestausuario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Opcion',
        ),
        migrations.DeleteModel(
            name='Pregunta',
        ),
        migrations.DeleteModel(
            name='RespuestaUsuario',
        ),
    ]
