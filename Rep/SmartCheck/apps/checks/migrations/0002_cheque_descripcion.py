# Generated by Django 3.1.1 on 2020-09-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheque',
            name='descripcion',
            field=models.CharField(default='Sin Datos', max_length=255),
            preserve_default=False,
        ),
    ]
