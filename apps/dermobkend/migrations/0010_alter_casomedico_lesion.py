# Generated by Django 4.1.5 on 2023-02-19 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dermobkend', '0009_remove_lesion_caso_casomedico_lesion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casomedico',
            name='lesion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesion_caso', to='dermobkend.lesion'),
        ),
    ]
