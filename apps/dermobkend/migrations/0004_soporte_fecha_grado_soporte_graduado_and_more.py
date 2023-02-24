# Generated by Django 4.1.5 on 2023-02-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dermobkend', '0003_remove_diagnostico_medico_remove_soporte_fecha_grado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soporte',
            name='fecha_grado',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='soporte',
            name='graduado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='soporte',
            name='institucion_educativa',
            field=models.TextField(default='NUNGUNA', max_length=150),
        ),
        migrations.AddField(
            model_name='soporte',
            name='nombre_programa',
            field=models.TextField(default='MEDICINA', max_length=150),
        ),
        migrations.AddField(
            model_name='soporte',
            name='validado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='soporte',
            name='descripcion',
            field=models.TextField(max_length=200, null=True),
        ),
    ]