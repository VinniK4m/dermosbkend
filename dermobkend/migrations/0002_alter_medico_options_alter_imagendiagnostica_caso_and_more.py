# Generated by Django 4.1.5 on 2023-01-25 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dermobkend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medico',
            options={'ordering': ['apellidos', '-nombres'], 'verbose_name': 'Medico', 'verbose_name_plural': 'Medicos'},
        ),
        migrations.AlterField(
            model_name='imagendiagnostica',
            name='caso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dermobkend.casomedico'),
        ),
        migrations.AlterModelTable(
            name='medico',
            table='docente',
        ),
    ]