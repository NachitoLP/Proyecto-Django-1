# Generated by Django 4.2.5 on 2023-09-11 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_departamento', '0002_alter_departamento_unique_together'),
        ('app_empleado', '0002_abilities_alter_empleado_options_empleado_abilities'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleado',
            new_name='Employee',
        ),
    ]
