# Generated by Django 4.1.5 on 2023-02-16 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dermobkend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='medico',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='dermobkend.medico'),
            preserve_default=False,
        ),
    ]