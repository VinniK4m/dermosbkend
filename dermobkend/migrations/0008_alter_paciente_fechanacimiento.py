# Generated by Django 4.1.5 on 2023-01-30 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dermobkend', '0007_alter_casomedico_options_alter_diagnostico_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
    ]