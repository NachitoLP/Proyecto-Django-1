# Generated by Django 4.2.5 on 2023-09-22 20:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_empleado', '0004_employee_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='observations',
            field=ckeditor.fields.RichTextField(default='Descripción'),
        ),
    ]