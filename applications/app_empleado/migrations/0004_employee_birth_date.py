# Generated by Django 4.2.5 on 2023-09-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_empleado', '0003_rename_empleado_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(default='1970-1-1', verbose_name='Fecha de nacimiento'),
        ),
    ]
