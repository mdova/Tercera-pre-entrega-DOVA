# Generated by Django 4.1.7 on 2023-02-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='marca',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='tipo',
        ),
        migrations.AddField(
            model_name='productos',
            name='fecha_de_carga',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='disponibilidad',
            field=models.BooleanField(),
        ),
    ]