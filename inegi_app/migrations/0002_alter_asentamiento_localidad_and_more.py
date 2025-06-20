# Generated by Django 5.2.2 on 2025-06-17 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inegi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asentamiento',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asentamientos', to='inegi_app.localidad'),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localidades', to='inegi_app.municipio'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='inegi_app.estado'),
        ),
    ]
