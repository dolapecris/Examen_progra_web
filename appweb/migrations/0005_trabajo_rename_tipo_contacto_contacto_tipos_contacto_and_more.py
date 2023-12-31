# Generated by Django 4.2.1 on 2023-07-10 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_mantencion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('domicilio', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('experiencia', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='trabajo')),
            ],
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='tipo_contacto',
            new_name='tipos_contacto',
        ),
        migrations.CreateModel(
            name='Rechazo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('tipo_rechazo', models.IntegerField(choices=[[0, 'Mala Redaccion'], [1, 'Faltas de Ortografia'], [2, 'Imagen Baja Calidad']])),
                ('mensaje', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='rechazo')),
                ('mecani', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.mecanico')),
            ],
        ),
    ]
