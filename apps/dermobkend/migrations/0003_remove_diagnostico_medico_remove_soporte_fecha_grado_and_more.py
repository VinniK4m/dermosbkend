# Generated by Django 4.1.5 on 2023-02-16 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dermobkend', '0002_diagnostico_medico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostico',
            name='medico',
        ),
        migrations.RemoveField(
            model_name='soporte',
            name='fecha_grado',
        ),
        migrations.RemoveField(
            model_name='soporte',
            name='graduado',
        ),
        migrations.RemoveField(
            model_name='soporte',
            name='institucion_educativa',
        ),
        migrations.RemoveField(
            model_name='soporte',
            name='nombre_programa',
        ),
        migrations.RemoveField(
            model_name='soporte',
            name='validado',
        ),
        migrations.AlterField(
            model_name='casomedico',
            name='estado',
            field=models.CharField(choices=[('CREADO', 'Creado'), ('ENREVISION', 'Reservado'), ('SELECCIONADO', 'Seleccionado'), ('LIBRE', 'Libre')], max_length=50),
        ),
        migrations.AlterField(
            model_name='soporte',
            name='descripcion',
            field=models.TextField(),
        ),
    ]